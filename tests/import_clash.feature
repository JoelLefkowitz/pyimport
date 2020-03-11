Feature: Detect static import name clashes:

Scenario: Directories containing modules that share names raise warnings  
    Given A path contains modules that may cause a clash
    When I call path_guard
    And The path is added to sys.path
    Then A warning is emitted
