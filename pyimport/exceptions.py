class PathDoesNotExist(Exception):
    def __init__(self, name) -> None:
        msg = f"The path '{name}' does not exist"
        super().__init__(msg)


class ModuleDoesNotExist(Exception):
    def __init__(self, name) -> None:
        msg = f"The module '{name}' does not exist"
        super().__init__(msg)


class ObjectDoesNotExist(Exception):
    def __init__(self, name) -> None:
        msg = f"The object '{name}' does not exist"
        super().__init__(msg)


class InitMissing(Exception):
    def __init__(self, folder) -> None:
        msg = f"The folder '{folder}' has no file called __init__.py"
        super().__init__(msg)
