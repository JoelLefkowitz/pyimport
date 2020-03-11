# coding=utf-8
"""Idempotent init.py guard feature tests."""

from pytest_bdd import (
    given,
    scenario,
    then,
    when,
)


@scenario("tests/init_guard.feature", "Import __init__.py")
def test_import___init__py():
    """Import __init__.py."""


@scenario("tests/init_guard.feature", "Missing __init__.py")
def test_missing___init__py():
    """Missing __init__.py."""


@scenario("tests/init_guard.feature", "__init__.py is not re-imported")
def test___init__py_is_not_reimported():
    """__init__.py is not re-imported."""


@given("__init__.py in the local directory has been imported")
def __init__py_in_the_local_directory_has_been_imported():
    """__init__.py in the local directory has been imported."""
    raise NotImplementedError


@given("__init__.py in the local directory has not been imported")
def __init__py_in_the_local_directory_has_not_been_imported():
    """__init__.py in the local directory has not been imported."""
    raise NotImplementedError


@given("__init__.py is not in the local directory")
def __init__py_is_not_in_the_local_directory():
    """__init__.py is not in the local directory."""
    raise NotImplementedError


@when("I call init_guard")
def i_call_init_guard():
    """I call init_guard."""
    raise NotImplementedError


@then("An InitMissing exception is raised")
def an_initmissing_exception_is_raised():
    """An InitMissing exception is raised."""
    raise NotImplementedError


@then("init_guard does not import __init__.py")
def init_guard_does_not_import___init__py():
    """init_guard does not import __init__.py."""
    raise NotImplementedError


@then("init_guard imports __init__.py")
def init_guard_imports___init__py():
    """init_guard imports __init__.py."""
    raise NotImplementedError
