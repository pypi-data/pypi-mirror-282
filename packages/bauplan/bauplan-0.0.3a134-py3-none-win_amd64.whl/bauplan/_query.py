"""
The module contains functions to launch SQL queries on Bauplan and retrieve
the result sets in a variety of formats (arrow Table, generator, file).
"""

import json
import os
from datetime import datetime
from typing import Any, Dict, Generator, Optional

import grpc
import pyarrow as pa
import pyarrow.flight as flight

from . import exceptions
from ._common import BAUPLAN_VERSION, _get_commander_and_metadata
from ._protobufs.bauplan_pb2 import TriggerRunRequest


def _iterate_flight_stream_batches(
    reader: flight.FlightStreamReader, max_rows: int | None = None
) -> Generator[pa.lib.RecordBatch, None, None]:
    rows = 0
    while True:
        try:
            if reader is None:
                raise exceptions.NoResultsFoundError('No results found')
            chunk: Optional[pa.lib.RecordBatch] = reader.read_chunk()
            if chunk is not None:
                batch: pa.lib.RecordBatch = chunk.data
                yield batch
                if max_rows:
                    rows += batch.num_rows
                    if rows >= max_rows:
                        raise StopIteration
            else:
                break
        except StopIteration:
            break


def _query(
    query: str,
    max_rows: int = 10,
    no_cache: bool = False,
    branch: str = 'main',
    connector: Optional[str] = None,
    connector_config_key: Optional[str] = None,
    connector_config_uri: Optional[str] = None,
    return_flight_stream: Optional[bool] = None,
    args: Optional[Dict[str, Any]] = None,
) -> pa.Table:
    """
    Execute a SQL query and return the results as a pyarrow.Table.

    If you prefer to return the raw FlightStreamReader, pass `return_flight_stream=True`.
    """
    if max_rows is not None:
        # max_rows limits
        if not isinstance(max_rows, int) or not (0 < max_rows < 100000000):
            raise ValueError('max_rows must be positive integer 1-100000000')

    # rebuild a query with the connector strings if specified
    # note that if the connector is not specified we get back the query as is
    query = _add_connector_strings_to_query(query, connector, connector_config_key, connector_config_uri)

    trigger_run_request: TriggerRunRequest = TriggerRunRequest(
        module_version=BAUPLAN_VERSION,
        args=args or {},
        query_for_flight=query,
        is_flight_query=True,
    )

    if no_cache:
        trigger_run_request.args['runner-cache'] = 'off'

    if branch:
        trigger_run_request.args['read-branch'] = branch

    client, metadata = _get_commander_and_metadata()

    job_id: TriggerRunRequest = client.TriggerRun(trigger_run_request, metadata=metadata)
    log_stream: grpc.Call = client.SubscribeLogs(job_id, metadata=metadata)
    flight_endpoint: Optional[str] = None
    for log in log_stream:
        if os.getenv('BPLN_DEBUG'):
            print(log)

        ev = log.runner_event
        if ev and ev.WhichOneof('event') == 'flight_server_start':
            flight_endpoint = log.runner_event.flight_server_start.endpoint
            break
    if not flight_endpoint:
        return None
    flight_client: flight.FlightClient = flight.FlightClient('grpc://' + flight_endpoint)
    options: flight.FlightCallOptions = flight.FlightCallOptions(
        headers=[(b'authorization', 'Bearer my_special_token'.encode())]
    )
    ticket: flight.Ticket = next(flight_client.list_flights(options=options)).endpoints[0].ticket
    reader: flight.FlightStreamReader = flight_client.do_get(ticket, options=options)

    if return_flight_stream:
        return reader
    if reader is None:
        raise exceptions.NoResultsFoundError('No results found')
    if max_rows:
        num_rows = 0
        stop = None
        data = None
        for batch in _iterate_flight_stream_batches(reader, max_rows):
            if stop:
                break
            for i in range(batch.num_rows):
                row = _row_to_dict(batch, i, batch.schema)
                if not data:
                    data = {k: [v] for k, v in row.items()}
                else:
                    for k, v in row.items():
                        data[k].append(v)
                if max_rows:
                    num_rows += 1
                    if num_rows >= max_rows:
                        stop = True
                        break
        return pa.table({k: v[:max_rows] for k, v in data.items()}, schema=batch.schema)

    return reader.read_all()


def _add_connector_strings_to_query(
    query: str,
    connector: Optional[str] = None,
    connector_config_key: Optional[str] = None,
    connector_config_uri: Optional[str] = None,
) -> str:
    """

    Add the connector strings to the query to allow the backend to direct the query to the correct engine.
    We assume that if the connector is not specified we use Bauplan as is; the other properties default to
    sensible values (check the docs for the details!).

    """
    if not connector:
        return query

    connector_string = f'-- bauplan: connector={connector}'
    connector_config_key_string = (
        f'-- bauplan: connector.config_key={connector_config_key}' if connector_config_key else ''
    )
    connector_config_uri_string = (
        f'-- bauplan: connector.config_uri={connector_config_uri}' if connector_config_uri else ''
    )

    return f'{connector_string}\n{connector_config_key_string}\n{connector_config_uri_string}\n{query}'


def _build_query_from_scan(
    table: str,
    columns: Optional[list] = None,
    filters: Optional[str] = None,
    limit: Optional[int] = None,
) -> str:
    """
    Take as input the arguments of the scan function and build a SQL query
    using SQLGlot.

    :meta private:

    """
    from sqlglot import select

    cols = columns or ['*']
    q = select(*cols).from_(table).where(filters)
    if limit:
        q = q.limit(limit)

    return q.sql()


def _scan(
    table: str,
    columns: Optional[list] = None,
    filters: Optional[str] = None,
    limit: Optional[int] = None,
    branch: str = 'main',
    connector: Optional[str] = None,
    connector_config_key: Optional[str] = None,
    connector_config_uri: Optional[str] = None,
    args: Optional[Dict] | None = None,
    **kwargs: Any,
) -> pa.Table:
    """
    Execute a table scan (with optional filters) and return the results as an arrow Table.
    Note that this function uses SQLGlot to compose a safe SQL query,
    and then internally defer to the query_to_arrow function for the actual scan.
    """
    q = _build_query_from_scan(table, columns, filters, limit)
    return _query(
        query=q,
        branch=branch,
        connector=connector,
        connector_config_key=connector_config_key,
        connector_config_uri=connector_config_uri,
        args=args,
        **kwargs,
    )


def _query_to_generator(
    query: str,
    max_rows: int = 10,
    no_cache: bool = False,
    branch: str = 'main',
    connector: Optional[str] = None,
    connector_config_key: Optional[str] = None,
    connector_config_uri: Optional[str] = None,
    args: Optional[Dict[str, Any]] = None,
) -> Generator[Dict[str, Any], None, None]:
    """
    Execute a SQL query and return the results as a generator, where each row is
    a Python dictionary.

    :param args: Arguments to pass to the query function.
    :param kwargs: Keyword arguments to pass to the query function.
    :yield: A dictionary representing a row of query results.
    """
    reader: flight.FlightStreamReader = _query(
        query=query,
        max_rows=max_rows,
        no_cache=no_cache,
        branch=branch,
        connector=connector,
        connector_config_key=connector_config_key,
        connector_config_uri=connector_config_uri,
        return_flight_stream=True,
        args=args,
    )
    if reader is None:
        raise exceptions.NoResultsFoundError('No results found')
    num_rows = 0
    stop = None
    for batch in _iterate_flight_stream_batches(reader, max_rows):
        if stop:
            break
        for i in range(batch.num_rows):
            yield _row_to_dict(batch, i, batch.schema)
            if max_rows:
                num_rows += 1
                if num_rows >= max_rows:
                    stop = True
                    break

    for batch in _iterate_flight_stream_batches(reader):
        for i in range(batch.num_rows):
            yield _row_to_dict(batch, i, batch.schema)


def _row_to_dict(
    batch: pa.lib.RecordBatch,
    row_index: int,
    schema: pa.lib.Schema,
) -> Dict[str, Any]:
    """
    Convert a row of a ``pyarrow.RecordBatch`` to a dictionary.

    :meta private:

    :param batch: The ``pyarrow.RecordBatch`` containing the row.
    :param row_index: The index of the row to convert.
    :param schema: The schema of the ``RecordBatch``.
    :return: A dictionary representing the row.
    """
    row: Dict[str, Any] = {}
    for j, name in enumerate(schema.names):
        column: pa.lib.ChunkedArray = batch.column(j)
        value = column[row_index].as_py()
        if isinstance(value, datetime):
            value = value.isoformat()
        row[name] = value
    return row


def _query_to_file(
    filename: str,
    query: str,
    max_rows: int = 10,
    no_cache: bool = False,
    branch: str = 'main',
    connector: Optional[str] = None,
    connector_config_key: Optional[str] = None,
    connector_config_uri: Optional[str] = None,
    args: Optional[Dict[str, Any]] = None,
) -> None:
    """
    Execute a SQL query and write the results to a file.
    """
    if filename.endswith('.json'):
        with open(filename, 'w') as outfile:
            outfile.write('[\n')
            first_row: bool = True
            for row in _query_to_generator(
                query=query,
                max_rows=max_rows,
                no_cache=no_cache,
                branch=branch,
                connector=connector,
                connector_config_key=connector_config_key,
                connector_config_uri=connector_config_uri,
                args=args,
            ):
                if not first_row:
                    outfile.write(',\n')
                    first_row = False
                outfile.write(json.dumps(row))
            outfile.write('\n]')
    else:
        raise ValueError('Only .json extension is supported for filename')
