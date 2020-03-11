Feature: Atomic resource getter

Scenario: A module is imported without affecting sys.path 
    When I call get_module
    Then get_module imports the module  
    And get_module leaves sys.path unchanged

Scenario: An object is retrieved without affecting sys.path 
    When I call get_object
    Then get_object returns the object   
    And get_object leaves sys.path unchanged

Scenario: Cannot get a module that does not exist
    Given A module does not exist
    When I call get_module
    Then A ModuleDoesNotExist exception is raised

Scenario: Cannot get an object from a module that does not exist
    Given A module does not exist
    When I call get_object
    Then A ModuleDoesNotExist exception is raised

Scenario: Cannot get an object that does not exist
    Given An object does not exist
    When I call get_object
    Then An ObjectDoesNotExist exception is raised
