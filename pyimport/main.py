import os, sys, inspect
from dataclasses import dataclass
from types import ModuleType

def path_guard(*rel_module_paths: str) -> None:
    frame = inspect.stack()[1]
    source_path = frame[0].f_code.co_filename

    for rel_module_path in rel_module_paths:
        module_path = os.path.join(source_path, rel_module_path)
    
        if not os.path.exists(module_path):
            raise (PathNotResolvable(module_path))

        if module_path not in sys.path:
            sys.path.append(module_path)

    # This solve ambiguity with static name clashes?
    # If at append time there is a file with the same name in two matching paths raise a warning
    # TODO


def get_resource(rel_resource_path: str) -> ModuleType:
    frame = inspect.stack()[1]
    source_path = frame[0].f_code.co_filename
    resource_path = os.path.join(source_path, rel_resource_path)

    if not os.path.exists(resource_path):
        raise (PathNotResolvable(resource_path))

    module_dir = os.path.dirname(os.path.normpath(resource_path))
    module_name = os.path.basename(os.path.normpath(resource_path))
    if module_name.endswith(".py"):
        module_name = module_name[:-3]

    with PathControl(module_dir):
        module = __import__(module_name)

    return module


<<<<<<< HEAD
=======
def init_guard() -> ModuleType:
    frame = inspect.stack()[1]
    source_path = frame[0].f_code.co_filename

    folder = os.path.dirname(source_path)
    contents = os.listdir(folder)

    if not "__init__.py" in contents:
        raise (InitNotFound(folder))
    else:
        return get_resource(os.path.join(folder, "__init__.py"))


>>>>>>> 0bd5829adcd375a8b5a66f2f44bd4469fcecd63b
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
    

