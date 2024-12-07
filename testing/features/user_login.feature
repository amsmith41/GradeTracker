Feature: User Registration
  Scenario: Log In
  Scenario: Log In
    Given we are at the home screen
    And we are logged out
    When we navigate to the login button
    And we enter TestUser into id_username
    And we enter pa$$wrd123 into id_password
    And we click the Login button
    Then we are at the dashboard

