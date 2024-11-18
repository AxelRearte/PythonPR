# config.py
from lib2to3.pgen2 import driver

from selenium import webdriver
from selenium.webdriver.common.by import By

LOGIN_URL = "https://practicetestautomation.com/practice-test-login/"
SUCCESS_URL = "https://practicetestautomation.com/logged-in-successfully/"
USERNAME = "student"
PASSWORD = "Password123"
SUCCESS_TEXT = "Logged In Successfully"
SUBMIT_BUTTON_XPATH = "//button[@id='submit']"

def click_element_by_xpath(driver, xpath):
    """
    Encuentra un elemento por su XPATH y realiza un clic en él.

    :param driver: El controlador de Selenium.
    :param xpath: El XPATH del elemento a encontrar.
    """
    element = driver.find_element(By.XPATH, xpath)
    element.click()