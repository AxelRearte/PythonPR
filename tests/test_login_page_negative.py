import time
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
#Yield is like return but i can keep typing below that
from tests.config import LOGIN_URL, click_element_by_xpath, SUBMIT_BUTTON_XPATH


class TestNegativeScenarios:

    @pytest.mark.login
    @pytest.mark.negative
    @pytest.mark.parametrize("username, password, expected_error_message", [("incorrectUser","Password123", "Your username is invalid!" ),
                                                                              ("student", "Password1234", "Your password is invalid!" )])
    def test_negative_login(self, driver, username, password, expected_error_message):
        # Open page
        # driver = webdriver.Chrome()
        driver.get(LOGIN_URL)

        # Type incorrect username student into Username field
        driver.find_element(By.ID, "username").send_keys(username)

        # Type password Password123 into Password field
        driver.find_element(By.ID, "password").send_keys(password)

        # Push Submit button
        click_element_by_xpath(driver, SUBMIT_BUTTON_XPATH)

        # Verify error message is displayed
        error_message_locator = driver.find_element(By.ID, "error")
        assert error_message_locator.is_displayed(), "Error message is not displayed, but it should"

        # Verify error message is displayed for username
        error_message = error_message_locator.text
        assert error_message == expected_error_message, "Error message is not expected"

    """
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
        """



