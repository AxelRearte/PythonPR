from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By


def get_username_element(driver: WebDriver):
    return driver.find_element(By.ID, "username")