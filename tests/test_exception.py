from telnetlib import EC
import pytest
from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class TestExceptions:

    """
    @pytest.mark.exception
    def test_no_such_element_exception(self, driver):
        # Open page
        driver.get("https://practicetestautomation.com/practice-test-exceptions/")

        # Click Add button
        add_button_locator = driver.find_element(By.ID, "add_btn")
        add_button_locator.click()


        # Verify Row 2 input field is displayed
        row_2_input_locator = driver.find_element(By.XPATH, "//div[@id='row2']/input")
        assert row_2_input_locator.is_displayed(), "Row 2 input should be displayed, but it's not"
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