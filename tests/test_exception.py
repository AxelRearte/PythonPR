import time
from lib2to3.fixes.fix_tuple_params import tuple_name
from telnetlib import EC
import pytest
from selenium import webdriver
from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.expected_conditions import presence_of_element_located
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC, wait

from page_objects.exceptions_page import ExceptionsPage


class TestExceptions:


    @pytest.mark.exceptions
    def test_no_such_element_exception(self, driver):
        exception_page = ExceptionsPage(driver)
        exception_page.open()
        exception_page.add_second_row()
        assert exception_page.is_row2_displayed(), "Row 2 input should be displayed, but it's not"

    @pytest.mark.exceptions
    def test_element_not_interactable_exception(self, driver):
        exception_page = ExceptionsPage(driver)
        exception_page.open()
        exception_page.add_second_row()
        exception_page.add_second_food("Hello")
        assert exception_page.get_confirmation_message() == "Row 2 was saved", "Confirmation message is not as expected"



    @pytest.mark.exceptions
    @pytest.mark.debug
    def test_invalid_state_element_exception(self, driver):
        exceptions_page = ExceptionsPage(driver)
        exceptions_page.open()
        exceptions_page.modify_row_1_input("Sushi")
        assert exceptions_page.get_confirmation_message() == "Row 1 was saved", "Confirmation message is not expected"


    @pytest.mark.exceptions
    def test_reference_exception(self, driver):
        # Open page
        driver.get("https://practicetestautomation.com/practice-test-exceptions/")

        #instrucion element
        instruction_locator = driver.find_element(By.ID, "instructions")

        # Click Add button
        add_button_locator = driver.find_element(By.ID, "add_btn")
        add_button_locator.click()

        #Verify instructions is not displayed
        wait = WebDriverWait(driver, 10)
        assert wait.until(EC.invisibility_of_element_located((By.ID, "instructions")),"Instruction text element should not be displayed")

    @pytest.mark.exceptions
    def test_timeout_exception(self, driver):
        # Open page
        driver.get("https://practicetestautomation.com/practice-test-exceptions/")

        # Click Add button
        add_button_locator = driver.find_element(By.ID, "add_btn")
        add_button_locator.click()

        # wait for 3 seconds to show the second row
        wait = WebDriverWait(driver, 3)
        row_2_input_element = wait.until(EC.visibility_of_element_located((By.XPATH, "//div[@id='row2']/input")),"Failed waiting for Row 2 input to be visible")

        # Verify Row 2 input field is displayed
        assert row_2_input_element.is_displayed(), "Row 2 input should be displayed, but it's not"






