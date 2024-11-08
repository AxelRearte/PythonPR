import time
from webbrowser import get
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager

@pytest.fixture()
def driver():
    print("Creating chrome driver")
    #my_driver = webdriver.Chrome()
    my_driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
    #my_driver = webdriver.Safari()
    yield my_driver
    print("Close chrome driver")
    my_driver.quit()

