@skip
Feature: Analyse the data from the csv 
    In order to access protected areas
    As a registered user
    I want to be able to log in

    @smoke
    Scenario: Successful login with valid credentials
        Given that the csv data is uploaded
        When the analyse method is invoked
        Then return a json object

    Scenario Outline: Login with different credentials
        Given I am on the login page
        When I enter "<username>" and "<password>"
        Then I should see "<message>"

        Examples:
            | username | password | message           |
            | valid   | valid    | Welcome!          |
            | invalid | valid    | Unknown user      |
            | valid   | invalid  | Incorrect password|