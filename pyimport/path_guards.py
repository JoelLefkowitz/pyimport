import os
import sys
import inspect

from .exceptions import PathDoesNotExist, InitMissing


def path_guard(*rel_module_paths: str) -> None:
    frame = inspect.stack()[1]
    source_path = frame[0].f_code.co_filename

    for rel_module_path in rel_module_paths:
        module_path = os.path.abspath(os.path.join(source_path, rel_module_path))

        if not os.path.exists(module_path):
            raise PathDoesNotExist(module_path)

        if module_path not in sys.path:
            sys.path.insert(0, module_path)


def init_guard() -> None:
    frame = inspect.stack()[1]
    source_path = frame[0].f_code.co_filename
    folder = os.path.dirname(source_path)

    if "__init__.py" not in os.listdir(folder):
        raise InitMissing(folder)
    else:
        return __import__(os.path.join(folder, "__init__.py"))
