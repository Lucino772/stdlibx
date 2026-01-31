from stdlibx.config._lib import load_config
from stdlibx.config._types import Loader
from stdlibx.config.loaders.env import EnvLoader
from stdlibx.config.loaders.file import FileLoader
from stdlibx.config.loaders.json import JsonLoader

__all__ = ["EnvLoader", "FileLoader", "JsonLoader", "Loader", "load_config"]

try:
    from stdlibx.config.loaders.yaml import YamlLoader

    __all__ += ["YamlLoader"]
except ImportError:
    pass
