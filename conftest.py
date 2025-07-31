import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

@pytest.fixture
def driver():
    service = Service("E:\\S_Demoqa\\drivers\\chromedriver-win64\\chromedriver.exe")
    driver = webdriver.Chrome(service=service)
    driver.maximize_window()
    yield driver  # this returns the driver to the test
    driver.quit()  # this runs after the test finishes
