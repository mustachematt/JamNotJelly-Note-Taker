Feature: login correctly
    
    Background: Navigate to Login page
        Given I am on "http://localhost:5000/login"
    
    Scenario: Verify error for empty username field
        Given "username" field is empty
        When I click on the Sign In button
        Then I see a "This field is required" in "usernameError"

    Scenario: Verify error for empty password field
        Given "password" field is empty
        When I click on the Sign In button
        Then I see a "This field is required" in "passwordError" 
    
    Scenario: Get correct error for incorrect username/password combination
        Given we type in "test1" in the "username" field
        And we type in "wrong" in the "password" field
        When I click on the Sign In button
        Then I see a "Invalid username or password" in "invalidnameorpassError"

    Scenario: Verify correct username and password works
        Given we type in "test1" in the "username" field
        And we type in "test" in the "password" field
        When I click on the Sign In button
        Then I should see the "What would you like to keep track of?"
    
    #current funcitnality is if you click remember me 
    #and close out of the browser when you open browser and 
    #navigate to site you are still logged in
    Scenario: Verify remember me button works 1
        Given we type in "test1" in the "username" field
        And we type in "test" in the "password" field
        And I click on "remember_me" field
        Then I click on the Sign In button
        And Close the browser
        #When I close browser and reopen browser 
        #And I navigate to "http://localhost:5000/mynotes"
        #Then I should see the "What would you like to keep track of?"
        