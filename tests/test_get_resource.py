# coding=utf-8
"""Atomic resource getter feature tests."""

from pytest_bdd import (
    given,
    scenario,
    then,
    when,
)


@scenario(
    "tests/get_resource.feature", "A module is imported without affecting sys.path"
)
def test_a_module_is_imported_without_affecting_syspath():
    """A module is imported without affecting sys.path."""


@scenario(
    "tests/get_resource.feature", "An object is retrieved without affecting sys.path"
)
def test_an_object_is_retrieved_without_affecting_syspath():
    """An object is retrieved without affecting sys.path."""


@scenario("tests/get_resource.feature", "Cannot get a module that does not exist")
def test_cannot_get_a_module_that_does_not_exist():
    """Cannot get a module that does not exist."""


@scenario(
    "tests/get_resource.feature",
    "Cannot get an object from a module that does not exist",
)
def test_cannot_get_an_object_from_a_module_that_does_not_exist():
    """Cannot get an object from a module that does not exist."""


@scenario("tests/get_resource.feature", "Cannot get an object that does not exist")
def test_cannot_get_an_object_that_does_not_exist():
    """Cannot get an object that does not exist."""


@given("A module does not exist")
def a_module_does_not_exist():
    """A module does not exist."""
    raise NotImplementedError


@given("An object does not exist")
def an_object_does_not_exist():
    """An object does not exist."""
    raise NotImplementedError


@when("I call get_module")
def i_call_get_module():
    """I call get_module."""
    raise NotImplementedError


@when("I call get_object")
def i_call_get_object():
    """I call get_object."""
    raise NotImplementedError


@then("A ModuleDoesNotExist exception is raised")
def a_moduledoesnotexist_exception_is_raised():
    """A ModuleDoesNotExist exception is raised."""
    raise NotImplementedError


@then("An ObjectDoesNotExist exception is raised")
def an_objectdoesnotexist_exception_is_raised():
    """An ObjectDoesNotExist exception is raised."""
    raise NotImplementedError


@then("get_module imports the module")
def get_module_imports_the_module():
    """get_module imports the module."""
    raise NotImplementedError


@then("get_module leaves sys.path unchanged")
def get_module_leaves_syspath_unchanged():
    """get_module leaves sys.path unchanged."""
    raise NotImplementedError


@then("get_object leaves sys.path unchanged")
def get_object_leaves_syspath_unchanged():
    """get_object leaves sys.path unchanged."""
    raise NotImplementedError


@then("get_object returns the object")
def get_object_returns_the_object():
    """get_object returns the object."""
    raise NotImplementedError
