import os
import sys
import inspect
from dataclasses import dataclass, field
from typing import Any, List
from types import ModuleType

from .exceptions import ModuleDoesNotExist, ObjectDoesNotExist


def get_module(rel_module_path: str) -> ModuleType:
    frame = inspect.stack()[1]
    source_path = frame[0].f_code.co_filename
    module_path = os.path.join(source_path, rel_module_path)

    if not os.path.exists(module_path):
        raise ModuleDoesNotExist(rel_module_path)

    module_dir = os.path.dirname(os.path.normpath(module_path))
    module_name = os.path.basename(os.path.normpath(module_path))

    if module_name.endswith(".py"):
        module_name = module_name[:-3]

    with PathControl(module_dir):
        module = __import__(module_name)

    return module


def get_object(object_name: str, rel_module_path: str) -> Any:
    module = get_module(rel_module_path)

    if not hasattr(module, object_name):
        raise ObjectDoesNotExist(object_name)
    else:
        return getattr(module, object_name)


@dataclass
class PathControl:
    module_dir: str
    exit_path: List[str] = field(default_factory=list)

    def __enter__(self) -> None:
        self.exit_path = sys.path.copy()
        sys.path.append(self.module_dir)

    def __exit__(self, type, value, tb) -> None:
        sys.path = self.exit_path.copy()
