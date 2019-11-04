Feature: Check that all the links work properly

    Scenario: Verify user can get to the login page by
        Given I am on "http://localhost:5000/"
        And I see "Jelly Lists, Digital List App" in the title
        When I click the "loginButton"
        Then I should be on the "Login" page
        And I should see the "login_box"