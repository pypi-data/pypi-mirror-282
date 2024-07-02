import importlib.metadata

__version__ = importlib.metadata.version(__package__ or __name__)

from mem0.client.main import Mem0  # noqa
