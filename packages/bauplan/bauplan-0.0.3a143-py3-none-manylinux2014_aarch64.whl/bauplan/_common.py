from __future__ import annotations

import datetime
import importlib.metadata
import os
import signal
from pathlib import Path
from typing import Any, List, Optional, Tuple

import grpc
import pyarrow  # type: ignore
import yaml  # type: ignore

from ._protobufs.bauplan_pb2 import CancelJobRequest, JobId
from ._protobufs.bauplan_pb2_grpc import CommanderServiceStub
from .bpln_proto.commander.service.v2 import service_pb2_grpc as v2

GRPC_METADATA_HEADER_API_KEY = 'x-bauplan-api-key'

BAUPLAN_VERSION: Optional[str] = None
try:
    BAUPLAN_VERSION = importlib.metadata.version('bauplan')
except Exception:
    print('`bauplan` package not found')


def _get_log_ts_str(val: int) -> str:
    """
    Output ISO timestamp to the decisecond from a nanosecond integer timestamp input.
    """
    return str(datetime.datetime.fromtimestamp(round(val / 1000000000, 2)))[:21]


def _get_catalog_host() -> str:
    addr: str = ''
    env = os.getenv('BPLN_ENV', '')
    if env == '':
        env = _load_default_config_profile().get('env')
    if env == 'local':
        addr = 'http://localhost:35432'
    elif env == 'dev':
        addr = 'https://catalog.use1.adev.bauplanlabs.com'
    elif env == 'qa':
        addr = 'https://catalog.use1.aqa.bauplanlabs.com'
    else:
        addr = 'https://catalog.use1.aprod.bauplanlabs.com'
    return addr


def _get_api_key(api_key: str | None = None) -> str:
    if api_key is None:
        api_key = ''
    if api_key == '':
        api_key = os.getenv('BAUPLAN_API_KEY', '')
    if api_key == '':
        api_key = _load_default_config_profile().get('api_key', '')
    if api_key == '':
        raise EnvironmentError(
            'No API key found in environment. Please update your ~/.bauplan/config.yml or set BAUPLAN_API_KEY.'
        )
    return api_key


def _get_env() -> str:
    env = os.getenv('BPLN_ENV', '')
    if env == '':
        env = _load_default_config_profile().get('env', '')
    else:
        return env
    if env == '':
        raise EnvironmentError('No Bauplan environment specified. Please update your ~/.bauplan/config.yml.')
    return env


def _get_commander_and_metadata(api_key: str | None) -> Tuple[CommanderServiceStub, List[Tuple[str, str]]]:
    conn: grpc.Channel = _dial_commander()
    client: CommanderServiceStub = CommanderServiceStub(conn)
    api_key = _get_api_key(api_key)
    metadata = [(GRPC_METADATA_HEADER_API_KEY, api_key)]
    return client, metadata


def _get_commander_v2_and_metadata(
    api_key: str | None,
) -> Tuple[v2.V2CommanderServiceStub, List[Tuple[str, str]]]:
    conn: grpc.Channel = _dial_commander()
    client = v2.V2CommanderServiceStub(conn)
    api_key = _get_api_key(api_key)
    metadata = [(GRPC_METADATA_HEADER_API_KEY, api_key)]
    return client, metadata


def _get_or_validate_branch(branch_name: str | None = None) -> str:
    """
    Default branch is the local active branch, or 'main'.
    """
    if branch_name is not None:
        if not isinstance(branch_name, str) or branch_name == '':
            raise ValueError('branch_name must be a non-empty string')
    else:
        branch_name = _load_default_config_profile().get('active_branch', 'main')
    return branch_name


def _load_default_config_profile() -> dict:
    home_dir = Path.home()
    config_path = home_dir / '.bauplan' / 'config.yml'

    if not config_path.is_file():
        return {}

    with open(config_path, 'r') as config_file:
        config_data = yaml.safe_load(config_file)

    return config_data.get('profiles', {}).get('default', {})


def _dial_commander() -> grpc.Channel:
    addr: str = ''
    env: Optional[str] = _get_env()
    if env == 'local':
        addr = 'localhost:2758'
    elif env == 'dev':
        addr = 'commander-poc.use1.adev.bauplanlabs.com:443'
    elif env == 'qa':
        addr = 'commander-poc.use1.aqa.bauplanlabs.com:443'
    else:
        addr = 'commander-poc.use1.aprod.bauplanlabs.com:443'
    creds: grpc.ChannelCredentials = grpc.ssl_channel_credentials()
    conn: grpc.Channel = grpc.secure_channel(addr, creds)
    return conn


class JobLifeCycleHandler:
    """
    Cancel jobs upon user or terminal interrupt.
    Also closes the flight client and grpc log stream connections.

    Try to cancel job, default timeout is 10 seconds.

    NOTE:
        This doesn't play nicely with threads.
        When we need that: https://stackoverflow.com/a/31667005
    """

    def __init__(
        self,
        job_id: JobId,
        client: CommanderServiceStub,
        metadata: Any,
        log_stream: grpc.Call = None,
        flight_client: pyarrow.flight.FlightClient = None,
        cancel_timeout: int = 10,  # seconds
    ) -> None:
        self.job_id = job_id
        self.client = client
        self.metadata = metadata
        self.cancel_timeout = cancel_timeout
        self.log_stream = log_stream
        self.flight_client = flight_client

    def __enter__(self) -> JobLifeCycleHandler:
        """
        Register signal handlers for SIGINT and SIGTERM
        """
        self.cancel_job_on_interrupt()
        return self

    def __exit__(self, *args, **kwargs) -> None:
        """
        Stop signal handling.
        NOTE signal.pause() does not work on Windows; see https://stackoverflow.com/a/77129638
        """
        pass

    def add_log_stream(self, log_stream: grpc.Call) -> None:
        self.log_stream = log_stream

    def add_flight_client(self, flight_client: pyarrow.flight.FlightClient) -> None:
        self.flight_client = flight_client

    def cancel_job_on_interrupt(self) -> None:
        """
        Cancel the job when user or terminal interrupts.
        Try for 5 seconds to cancel the job.
        """

        def complete_handler(sig: Any, frame: Any) -> None:
            pass

        def timeout_handler(sig: Any, frame: Any) -> None:
            if os.getenv('BPLN_DEBUG'):
                print(f'Could not cancel job; jobId: {self.job_id.id}; message')
            # return

        def cancel_handler(sig: Any, frame: Any) -> None:
            if os.getenv('BPLN_DEBUG'):
                print(f'\nReceived interrupt signal {sig}')
                print(f'Canceling job: {self.job_id.id}')
            signal.signal(signal.SIGALRM, timeout_handler)
            signal.signal(signal.SIGCONT, complete_handler)
            signal.alarm(self.cancel_timeout)
            try:
                if self.log_stream:
                    self.log_stream.cancel()
                if self.flight_client:
                    self.flight_client.close()
                response = self.client.CancelJob(CancelJobRequest(job_id=self.job_id), metadata=self.metadata)
            except Exception as e:
                raise e
            finally:
                # tell signal to stop waiting for a SIGALARM
                os.kill(os.getpid(), signal.SIGCONT)

            if os.getenv('BPLN_DEBUG'):
                print('Canceled job:')
                print(f'    id: {self.job_id.id}')
                print(f'    status: {response.status}')
                print(f'    message: {response.message}')

        signal.signal(signal.SIGINT, cancel_handler)
        signal.signal(signal.SIGTERM, cancel_handler)
