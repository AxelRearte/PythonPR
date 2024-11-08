import time
from webbrowser import get
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

@pytest.fixture()
def driver():
    print("Creating chrome driver")
    my_driver = webdriver.Chrome()
    yield my_driver
    print("Close chrome driver")
    my_driver.quit()