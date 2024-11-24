import time
from pydoc import browse
from webbrowser import get
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service as FirefoxService
from urllib3 import request
from webdriver_manager.firefox import GeckoDriverManager
import pytest
from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager

@pytest.fixture(params=["chrome"])  # Solo ejecutamos con Chrome
def driver(request):
    browser = request.param
    print(f"Creating {browser} driver")
    if browser == "chrome":
        my_driver = webdriver.Chrome()
    # Comentamos la parte de Firefox
    # elif browser == "firefox":
    #     my_driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
    else:
        raise TypeError(f"Expected 'chrome', but got {browser}")
    # my_driver = webdriver.Safari()  # Si se desea, se puede descomentar para Safari
    #my_driver.implicitly_wait(10)
    yield my_driver
    print(f"Closing {browser} driver")
    my_driver.quit()

def pytest_addoption(parser):
    parser.addoption(
        "--browser", action="store", default="chrome", help="browser to execute tests(chrome or firefox)"
    )

