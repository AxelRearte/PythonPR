import time
from webbrowser import get

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

from webdriver_manager.chrome import ChromeDriverManager

#Yield is like return but i can keep typing below that
@pytest.fixture()
def driver():
    print("Creating chrome driver")
    my_driver = webdriver.Chrome()
    yield my_driver
    print("Close chrome driver")
    my_driver.quit()



class TestNegativeScenarios:

    @pytest.mark.login
    @pytest.mark.negative
    def test_negative_username(self, driver):
        # Open page
        #driver = webdriver.Chrome()
        driver.get("https://practicetestautomation.com/practice-test-login/")

        # Type incorrect username student into Username field
        username_locator = driver.find_element(By.ID, "username")
        username_locator.send_keys("incorrectUser")

        # Type password Password123 into Password field
        password_locator = driver.find_element(By.ID, "password")
        password_locator.send_keys("Password123")

        # Push Submit button
        submit_button_locator = driver.find_element(By.XPATH, "//button[@id='submit']")
        submit_button_locator.click()
        time.sleep(2)

        #Verify error message is displayed
        error_message_locator = driver.find_element(By.ID, "error")
        assert error_message_locator.is_displayed(), "Error message is not displayed, but it should"

        # Verify error message is displayed for username
        error_message = error_message_locator.text
        assert error_message == "Your username is invalid!", "Error message is not expected"

    @pytest.mark.login
    @pytest.mark.negative
    def test_negative_password(self, driver):
        # Open page
        #driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        driver.get("https://practicetestautomation.com/practice-test-login/")

        # Type username student into Username field
        username_locator = driver.find_element(By.ID, "username")
        username_locator.send_keys("student")

        # Type incorrect password Password123 into Password field
        password_locator = driver.find_element(By.ID, "password")
        password_locator.send_keys("Password1234")

        # Push Submit button
        submit_button_locator = driver.find_element(By.XPATH, "//button[@id='submit']")
        submit_button_locator.click()
        time.sleep(2)

        # Verify error message is displayed
        error_message_locator = driver.find_element(By.ID, "error")
        assert error_message_locator.is_displayed(), "Error message is not displayed, but it should"

        # Verify error message is displayed for username
        error_message = error_message_locator.text
        assert error_message == "Your password is invalid!", "Error message is not expected"
