Feature: Idempotent path guard

Scenario: A path is added to sys.path
    Given A path is not already in sys.path
    When I call path_guard
    Then path_guard adds path to sys.path

Scenario: A path present in sys.path is not added again
    Given A path is already in sys.path
    When I call path_guard
    Then path_guard does not add path to sys.path

Scenario: Should not add a path that does not yet exist
    Given A path does not exist
    When I call path_guard
    Then A PathDoesNotExist exception is raised
