from selenium import webdriver
from selenium.webdriver.common.by import By
from dotenv import load_dotenv
import os

from .project import find_projects

# Load environment variables from .env file
load_dotenv()

# Access environment variables
user = os.getenv("USER")
password = os.getenv("PASSWORD")


def login_as_user():
    # Initialize a Chrome WebDriver instance
    driver = webdriver.Chrome()
    url = 'https://vav.unob.cz/auth/login'
    driver.get(url)
    try:
        driver.find_element(by=By.NAME, value='username').send_keys(user)
        driver.implicitly_wait(0.5)
        driver.find_element(by=By.NAME, value='password').send_keys(password)
        driver.implicitly_wait(0.5)
        driver.find_element(by=By.NAME, value='login').submit()
        
        find_projects(driver)
        

        input("Press Enter to continue...")

    finally:
        # Close the WebDriver
        driver.quit()