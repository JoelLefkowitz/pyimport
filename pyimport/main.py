import os, sys
from dataclasses import dataclass
from types import ModuleType


def path_guard(abs_file_path: str, module_path: str) -> None:
    abs_module_path = os.path.abspath(os.path.join(abs_file_path, module_path))

    if not os.path.exists(module_path):
        raise (PathNotResolvable(module_path))

    if abs_module_path not in sys.path:
        sys.path.append(abs_module_path)


def init_guard(abs_file_path: str) -> ModuleType:
    folder = os.path.dirname(abs_file_path)
    contents = os.listdir(folder)
    if not "__init__.py" in contents:
        raise (InitNotFound(folder))
    else:
        return get_resource(os.path.join(folder, "__init__.py"))


def get_resource(abs_resource_path: str) -> ModuleType:
    if not os.path.exists(abs_resource_path):
        raise (PathNotResolvable(abs_resource_path))

    module_dir = os.path.dirname(os.path.normpath(abs_resource_path))
    module_name = os.path.basename(os.path.normpath(abs_resource_path))
    if module_name.endswith(".py"):
        module_name = module_name[:-3]

    with PathControl(module_dir):
        module = __import__(module_name)

    return module


@dataclass
class PathControl:
    module_dir: str

    def __enter__(self) -> None:
        sys.path.append(self.module_dir)

    def __exit__(self, type, value, tb) -> None:
        sys.path.remove(self.module_dir)


class PathNotResolvable(Exception):
    def __init__(self, name) -> None:
        msg = f"The path '{name}' is not resolvable"
        super().__init__(msg)


class InitNotFound(Exception):
    def __init__(self, folder) -> None:
        msg = f"The folder '{folder}' has no file called __init__.py"
        super().__init__(msg)
