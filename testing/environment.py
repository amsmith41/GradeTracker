from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

def before_all(context):
    chrome_options = Options()
    chrome_options.add_argument("--start-maximized")  # Start browser maximized
    chrome_options.add_argument("--disable-notifications")  # Disable notifications
    #chrome_options.add_argument("--headless")  # Run in headless mode if you don't want a visible browser
    chrome_options.add_argument("--disable-gpu")  # Disable GPU (useful in headless mode)
    chrome_options.add_argument("--no-sandbox")  # No sandbox for Docker
    chrome_options.add_argument("--disable-dev-shm-usage")  # Overcome limited resource problems in Docker
    service = Service(ChromeDriverManager().install())
    context.driver = webdriver.Chrome(service=service, options=chrome_options)


def before_scenario(context, scenario):
    context.driver.get("http://127.0.0.1:8000/")

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



def after_all(context):
    context.driver.close()