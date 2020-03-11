# coding=utf-8
"""Idempotent path guard feature tests."""

from pytest_bdd import (
    given,
    scenario,
    then,
    when,
)


@scenario('tests/path_guard.feature', 'A path is added to sys.path')
def test_a_path_is_added_to_syspath():
    """A path is added to sys.path."""


@scenario('tests/path_guard.feature', 'A path present in sys.path is not added again')
def test_a_path_present_in_syspath_is_not_added_again():
    """A path present in sys.path is not added again."""


@scenario('tests/path_guard.feature', 'Should not add a path that does not yet exist')
def test_should_not_add_a_path_that_does_not_yet_exist():
    """Should not add a path that does not yet exist."""


@given('A path does not exist')
def a_path_does_not_exist():
    """A path does not exist."""
    raise NotImplementedError


@given('A path is already in sys.path')
def a_path_is_already_in_syspath():
    """A path is already in sys.path."""
    raise NotImplementedError


@given('A path is not already in sys.path')
def a_path_is_not_already_in_syspath():
    """A path is not already in sys.path."""
    raise NotImplementedError


@when('I call path_guard')
def i_call_path_guard():
    """I call path_guard."""
    raise NotImplementedError


@then('A PathDoesNotExist exception is raised')
def a_pathdoesnotexist_exception_is_raised():
    """A PathDoesNotExist exception is raised."""
    raise NotImplementedError


@then('path_guard adds path to sys.path')
def path_guard_adds_path_to_syspath():
    """path_guard adds path to sys.path."""
    raise NotImplementedError


@then('path_guard does not add path to sys.path')
def path_guard_does_not_add_path_to_syspath():
    """path_guard does not add path to sys.path."""
    raise NotImplementedError

