Feature: User Registration
  Scenario: Create Account
    Given we are at the home screen
    And we are logged out
    When we navigate to the register button
    And we enter TestUser into id_username
    And we enter email@example.com into id_email
    And we enter pa$$wrd123 into id_password1
    And we enter pa$$wrd123 into id_password2
    And we click the Sign Up button
    Then we are at the home screen