# coding=utf-8
"""Detect static import name clashes: feature tests."""

from pytest_bdd import (
    given,
    scenario,
    then,
    when,
)


@scenario('tests/import_clash.feature', 'Directories containing modules that share names raise warnings')
def test_directories_containing_modules_that_share_names_raise_warnings():
    """Directories containing modules that share names raise warnings."""


@given('A path contains modules that may cause a clash')
def a_path_contains_modules_that_may_cause_a_clash():
    """A path contains modules that may cause a clash."""
    raise NotImplementedError


@when('I call path_guard')
def i_call_path_guard():
    """I call path_guard."""
    raise NotImplementedError


@when('The path is added to sys.path')
def the_path_is_added_to_syspath():
    """The path is added to sys.path."""
    raise NotImplementedError


@then('A warning is emitted')
def a_warning_is_emitted():
    """A warning is emitted."""
    raise NotImplementedError

