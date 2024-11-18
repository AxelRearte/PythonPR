from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait

from tests.config import USERNAME, click_element_by_xpath, PASSWORD, SUBMIT_BUTTON_XPATH
from tests.conftest import driver
from selenium.webdriver.support import expected_conditions as EC, wait


class LoginPage:
    __url = "https://practicetestautomation.com/practice-test-login/"
    __username_field = (By.ID, "username")
    __password_field = (By.ID, "password")
    __submit_button = (By.XPATH, "//button[@id='submit']")

    def __init__(self, driver: WebDriver):
        self._driver = driver

    def open(self):
        self._driver.get(self.__url)

    def execute_login(self, username: str , password: str):
        wait = WebDriverWait(self._driver,10)
        wait.until(EC.visibility_of_element_located(self.__username_field))
        self._driver.find_element(By.ID, "username").send_keys(USERNAME)
        wait.until(EC.visibility_of_element_located(self.__password_field))
        self._driver.find_element(By.ID, "password").send_keys(PASSWORD)
        wait.until(EC.visibility_of_element_located(self.__submit_button))
        click_element_by_xpath(self._driver, SUBMIT_BUTTON_XPATH)
