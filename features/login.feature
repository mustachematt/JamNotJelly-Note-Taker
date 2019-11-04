Feature: login correctly
    
    Background: Navigate to Login page
        Given I am on "http://localhost:5000/login"
    
    Scenario: Verify error for empty username field
        Given "username" field is empty
        When I click on the "Sign In" button
        Then I see a "This field is required" "nameError"

    Scenario: Verify error for empty password field
        Given "password" field is empty
        When I click on the "Sign In" button
        Then I see a "This field is required" "passwordError" 


        
        


