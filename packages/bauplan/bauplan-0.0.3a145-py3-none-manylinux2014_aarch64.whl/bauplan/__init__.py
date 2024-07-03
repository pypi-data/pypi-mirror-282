import sys

if sys.version_info[:2] >= (3, 8):
    from importlib import metadata
else:
    import importlib_metadata as metadata  # type: ignore

from . import exceptions, helpers, schema, standard_expectations, store
from ._classes import Model
from ._client import Client
from ._decorators import expectation, model, pyspark, python, resources, synthetic_model
from ._import import ApplyPlanState, PlanImportState
from ._parameters import Parameter
from ._run import JobStatus, RunState

__version__ = metadata.version(__package__ or 'bauplan')

del metadata

__all__ = [
    'ApplyPlanState',
    'Client',
    'JobStatus',
    'Model',
    'Parameter',
    'PlanImportState',
    'RunState',
    '__version__',
    'exceptions',
    'expectation',
    'helpers',
    'model',
    'pyspark',
    'python',
    'resources',
    'schema',
    'standard_expectations',
    'store',
    'synthetic_model',
]
