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


class TestExceptions:


    @pytest.mark.exceptions
    def test_no_such_element_exception(self, driver):
        # Open page
        driver.get("https://practicetestautomation.com/practice-test-exceptions/")

        # Click Add button
        add_button_locator = driver.find_element(By.ID, "add_btn")
        add_button_locator.click()

        #Adding a WebDriverWait method and disable on fixture()
        wait = WebDriverWait(driver, 10)
        row_2_input_element = wait.until(EC.presence_of_element_located((By.XPATH, "//div[@id='row2']/input")))


        # Verify Row 2 input field is displayed
        assert row_2_input_element.is_displayed(), "Row 2 input should be displayed, but it's not"


    @pytest.mark.exceptions
    @pytest.mark.debug
    def test_element_not_interactable_exception(self, driver):
        # Open page
        driver.get("https://practicetestautomation.com/practice-test-exceptions/")

        # Click Add button
        add_button_locator = driver.find_element(By.ID, "add_btn")
        add_button_locator.click()

        #Adding a WebDriverWait method and disable on fixture()
        wait = WebDriverWait(driver, 10)
        row_2_input_element = wait.until(EC.presence_of_element_located((By.XPATH, "//div[@id='row2']/input")))


        # Verify Row 2 input field is displayed
        assert row_2_input_element.is_displayed(), "Row 2 input should be displayed, but it's not"

        #Type Text
        row_2_input_element.send_keys("Hello")

        #Find Locator of button save
        #Find a unique locator of button save $x("//div[@id='row2']/button[@name='Save']")
        save_button_locator = driver.find_element(By.XPATH, "//div[@id='row2']/button[@name='Save']")
        save_button_locator.click()

        #Confirmation text locator
        confirmation_locator = driver.find_element(By.ID, "confirmation")
        assert confirmation_locator.text == "Row 2 was saved", "Confirmation message is not as expected"

    @pytest.mark.exceptions
    @pytest.mark.invalidstate
    def test_invalid_state_element_exception(self, driver):
        # Open page
        driver.get("https://practicetestautomation.com/practice-test-exceptions/")

        # Click Add button
        edit_button_locator = driver.find_element(By.ID, "edit_btn")
        edit_button_locator.click()

        #Find text locator and clear value
        row_1_input_element = driver.find_element(By.XPATH, "//div[@id='row1']/input")
        wait = WebDriverWait(driver, 10)
        wait.until(EC.element_to_be_clickable(row_1_input_element))
        row_1_input_element.clear()

        row_1_input_element.send_keys("Sushi")

        #Save button
        save_button_locator = driver.find_element(By.ID, "save_btn")
        save_button_locator.click()

        # Confirmation text locator
        confirmation_locator = wait.until(EC.visibility_of_element_located((By.ID, "confirmation")))
        confirmation_locator = driver.find_element(By.ID, "confirmation")
        assert confirmation_locator.text == "Row 1 was saved", "Confirmation message is not as expected"

    @pytest.mark.exceptions
    @pytest.mark.referenceexcepetion
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
    @pytest.mark.timeout
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






