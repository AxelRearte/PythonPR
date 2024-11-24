import time
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService

from page_objects.logged_in_successfully import LoggedInSuccessfullyPage
from page_objects.login_page import LoginPage
from tests.config import LOGIN_URL, SUCCESS_URL, USERNAME, PASSWORD, SUCCESS_TEXT, click_element_by_xpath, SUBMIT_BUTTON_XPATH


class TestPositiveScenarios:
#This is a comment update.
    @pytest.mark.login
    @pytest.mark.positive
    def test_positive_login(self, driver):
        login_page = LoginPage(driver)
        login_page.open()
        login_page.execute_login("student", "Password123")
        # Verify new page URL contains practicetestautomation.com/logged-in-successfully/
        logged_in_page = LoggedInSuccessfullyPage(driver)
        assert logged_in_page.expected_url == login_page.current_url, "Actual url is not the same as expected"
        assert logged_in_page.header == "Logged In Successfully", "Header is not expected"
        assert logged_in_page.is_logout_button_displayed(), "Logout button should be visible"

