import string

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait

from page_objects.base_page import BasePage
from tests.config import USERNAME, click_element_by_xpath, PASSWORD, SUBMIT_BUTTON_XPATH
from tests.conftest import driver
from selenium.webdriver.support import expected_conditions as EC, wait


class ExceptionsPage(BasePage):
    __url = "https://practicetestautomation.com/practice-test-exceptions/"
    __add_button_locator = (By.ID, "add_btn")
    __row_1_input_element = (By.XPATH, "//div[@id='row1']/input")
    __row_2_input_element = (By.XPATH, "//div[@id='row2']/input")
    __row_1_save_button = (By.XPATH, "//div[@id='row1']/button[@name='Save']")
    __row_2_save_button = (By.XPATH, "//div[@id='row2']/button[@name='Save']")
    __row_1_edit_button = (By.ID, "edit_btn")
    __instruction_locator = (By.ID, "instructions")
    __confirmation_element = (By.ID, "confirmation")

    def __init__(self, driver: WebDriver):
        super().__init__(driver)

    def open(self):
        super()._open_url(self.__url)

    def add_second_row(self):
        super()._click(self.__add_button_locator)
        super()._wait_until_element_is_visible(self.__row_2_input_element)

    def execute_login(self, username: str, password: str):
        super()._type(self.__username_field, username)
        super()._type(self.__password_field, password)
        super()._click(self.__submit_button)

    def get_error_message(self)-> str:
        return super()._get_text(self.__error_message, 3)

    def is_row2_displayed(self)-> bool:
        return super()._is_displayed(self.__row_2_input_element)

    def add_second_food(self, food: string):
        super()._type(self.__row_2_input_element, food)
        super()._click(self.__row_2_save_button)
        super()._wait_until_element_is_visible(self.__confirmation_element)

    def get_confirmation_message(self)->str:
        return  super()._get_text(self.__confirmation_element, time = 3)

    def modify_row_1_input(self, food: str):
        super()._click(self.__row_1_edit_button)
        super()._wait_until_element_is_clickable(self.__row_1_input_element)
        super()._clear(self.__row_1_input_element)
        super()._type(self.__row_1_input_element, food)
        super()._click(self.__row_1_save_button)
        super()._wait_until_element_is_visible(self.__confirmation_element)



