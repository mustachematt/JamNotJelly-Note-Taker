Feature: login correctly

    Scenario: Verify we can get to the login page
        Given I am on "http://localhost:5000/"
        And I see "Jelly Lists, Digital List App" in the title
        When I click the "loginButton"
        Then I should be on the "Login" page
        And I should see the "apple"


