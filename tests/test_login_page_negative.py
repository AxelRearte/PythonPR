import time
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

from page_objects.login_page import LoginPage
#Yield is like return but i can keep typing below that
from tests.config import LOGIN_URL, click_element_by_xpath, SUBMIT_BUTTON_XPATH


class TestNegativeScenarios:

    @pytest.mark.login
    @pytest.mark.negative
    @pytest.mark.parametrize("username, password, expected_error_message", [("incorrectUser","Password123", "Your username is invalid!" ),
                                                                              ("student", "Password1234", "Your password is invalid!" )])

    def test_negative_login(self, driver, username, password, expected_error_message):
        login_page = LoginPage(driver)
        login_page.open()
        login_page.execute_login(username, password)
        time.sleep(2)
        assert login_page.get_error_message() == expected_error_message





