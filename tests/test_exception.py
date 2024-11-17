import time
from lib2to3.fixes.fix_tuple_params import tuple_name
from telnetlib import EC
import pytest
from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.expected_conditions import presence_of_element_located
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



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


    """
    @pytest.mark.exceptions
    def test_no_such_element_exception(self, driver):
        # Open page
        driver.get("https://practicetestautomation.com/practice-test-exceptions/")

        # Click Add button
        add_button_locator = driver.find_element(By.ID, "add_btn")
        add_button_locator.click()

        # Esperar a que el campo de entrada de la fila 2 esté presente
        try:
            row_2_input_locator = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, "//div[@id='row2']/input"))
            )
        except TimeoutException:
            print("Timeout: El elemento no está presente en la página.")
            assert False  # o maneja la excepción como desees

        # Si el elemento es encontrado, puedes interactuar con él aquí
        row_2_input_locator.send_keys("Texto de prueba")
    """
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

