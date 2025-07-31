from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from pages.ElementsPage.textbox_page import TextBoxPage
#import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


# Set up driver
def test_textbox_form():
    service = Service("E:\\S_Demoqa\\drivers\\chromedriver-win64\\chromedriver.exe")
    driver = webdriver.Chrome(service=service)
    driver.maximize_window()

    # Create page object
    text_box = TextBoxPage(driver)

    # Use page methods
    text_box.open()
    text_box.fill_form("Bipashna", "bipashna@example.com", "Lalitpur", "Kathmandu")
    text_box.submit()

    # Wait and get results
    # time.sleep(2)
    WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.ID, "name"))
    )
    assert text_box.get_output_name() == "Name:Bipashna"
    print(text_box.get_output_email())

    # Close
    driver.quit()
