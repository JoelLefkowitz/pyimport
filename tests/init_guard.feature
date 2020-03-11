Feature: Idempotent init.py guard

Scenario: Import __init__.py
    Given __init__.py in the local directory has not been imported
    When I call init_guard
    Then init_guard imports __init__.py

Scenario: __init__.py is not re-imported
    Given __init__.py in the local directory has been imported
    When I call init_guard
    Then init_guard does not import __init__.py

Scenario: Missing __init__.py
    Given __init__.py is not in the local directory
    When I call init_guard
    Then An InitMissing exception is raised