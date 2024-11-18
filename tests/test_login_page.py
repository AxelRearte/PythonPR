import time
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService

from tests.config import LOGIN_URL, SUCCESS_URL, USERNAME, PASSWORD, SUCCESS_TEXT, click_element_by_xpath, SUBMIT_BUTTON_XPATH


class TestPositiveScenarios:
#This is a comment update.
    @pytest.mark.login
    @pytest.mark.positive
    def test_positive_login(self, driver):
        #Open Browser
        #Remove this line because the fixture is used
        #driver = webdriver.Chrome()

        #Open page
        driver.get(LOGIN_URL)
        #Type username student into Username field
        driver.find_element(By.ID, "username").send_keys(USERNAME)

        #Type password Password123 into Password field
        driver.find_element(By.ID, "password").send_keys(PASSWORD)

        #Push Submit button
        #driver.find_element(By.XPATH, "//button[@id='submit']").click()
        click_element_by_xpath(driver, SUBMIT_BUTTON_XPATH)

        #Verify new page URL contains practicetestautomation.com/logged-in-successfully/
        assert driver.current_url == SUCCESS_URL

        #Verify new page contains expected text ('Congratulations' or 'successfully logged in')
        success_text = driver.find_element(By.TAG_NAME, "h1").text
        assert success_text == SUCCESS_TEXT

        #Verify button Log out is displayed on the new page
        assert driver.find_element(By.LINK_TEXT, "Log out").is_displayed()

        """"""""""
        Test case 1: Positive LogIn test
        
        
        
        Push Submit button
        
        Verify new page contains expected text ('Congratulations' or 'successfully logged in')
        Verify button Log out is displayed on the new page
        """""""""""