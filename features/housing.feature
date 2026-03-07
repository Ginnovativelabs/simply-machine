Feature: Validate housing.csv column data types
  As a data engineer
  I want to check that housing.csv columns have the expected data types
  So that downstream analysis is correct

  Background:
    Given the dataset "datasets/housing/housing.csv" is loaded

  Scenario: Check numeric columns
    When the Anaylser object is initiated with the dataset
    Then the column "median_income" should be "numeric"

  Scenario: Check categorical / string columns
    When the Anaylser object is initiated with the dataset
    Then the column "ocean_proximity" should be "categorical"

  Scenario: Check integer columns
    When the Anaylser object is initiated with the dataset
    Then the column "total_rooms" should be "integer"
    And the column "housing_median_age" should be "integer"
  
  Scenario: Checking data dictory creation with column names and data types
    When the Anaylser object is initiated with the dataset
    Then the key "total_rooms" should have the value "integer"
    And the key "housing_median_age" should have the value "integer"
    And the key "ocean_proximity" should have the value "categorical"
  
  Scenario: Checking None / NaN values 
    When the Anaylser object is initiated with the dataset
    Then the column "total_rooms" should have zero NaN values

Scenario: NaN value counts data dictory
    When the Anaylser object is initiated with the dataset
    Then the key "total_rooms" should have no NaN values
    And the key "total_bedrooms" should have NaN values