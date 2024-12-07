from behave import step
from hamcrest import assert_that, is_, is_not
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
import time

@step(u'we are logged out')
@step(u'we are at the home screen')
def step_impl(context):

    logged_in = True

    # Log out if we are logged in
    h1_elements = context.driver.find_elements(By.TAG_NAME, "h1")
    for h1 in h1_elements:
        if "Welcome to our Grade Traceker" in h1.text:
            logged_in = False
            break

    if logged_in:
        # Locate the Logout button by class and text
        buttons = context.driver.find_elements(By.CLASS_NAME, "nav-item.nav-link.btn.btn-link")
        for button in buttons:
            if button.text.strip() == "Logout":
                button.click()
                break

    if logged_in:
        time.sleep(5)
    assert_that(logged_in, is_(False), "We are not on the home screen")


# Log out if we are logged in
@step(u'we are at the dashboard')
def step_impl(context):
    try:
        element = context.driver.find_element(
            "xpath", "//p[@class='text-muted' and contains(text(), 'We care about your academic success')]"
        )
    except NoSuchElementException:
        assert_that(False, is_(True), f"We are not on the dashboard screen")



@step(u'we navigate to the {button_text} button')
def step_impl(context, button_text):
    try:
        button = context.driver.find_element(By.XPATH, f'//a[@class="nav-item nav-link" and @href="/{button_text}/"]')
        button.click()
    except NoSuchElementException:
        assert_that(False, is_(True), f"The nav button '{button_text}' was not found")
        

@step(u'we click the {button_text} button')
def step_impl(context, button_text):
    try:
        button = context.driver.find_element(By.XPATH, f"//button[@class='btn btn-outline-info' and @type='submit' and text()='{button_text}']")
        button.click()
    except NoSuchElementException:
        assert_that(False, is_(True), f"The button '{button_text}' was not found")


@step(u'we enter {value} into {element_id}')
def step_impl(context, value, element_id):
    try:
        element = context.driver.find_element(By.ID, element_id)
        element.send_keys(value)

    except NoSuchElementException:
        assert_that(False, is_(True), f"The element '{element_id}' was not found")


