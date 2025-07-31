from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from pages.FormsPage.form_page import FormPage
import time




# Set up driver
def test_form_form():
    service = Service("E:\\S_Demoqa\\drivers\\chromedriver-win64\\chromedriver.exe")
    driver = webdriver.Chrome(service=service)
    driver.maximize_window()

    # Create page object
    form = FormPage(driver)

    # Use page methods
    form.open()
    form.fill_form("Bipashna", "Maharjan", "bipashna@example.com", "Computer Science", "Nepal")
    form.select_gender_male()
    form.select_mobile("9876543210")
    form.select_hobbies("Sports", "Music", "reading")
    form.upload_picture(r"E:\S_Demoqa\images\logo.png")
    form.select_state("NCR")
    form.select_city("Delhi")
    form.submit()

    
    assert form.get_output_fullname() == "Bipashna Maharjan"
    assert form.get_output_email() == "bipashna@example.com"
    assert form.get_output_gender() == "Male"
    assert form.get_output_mobile() =="9876543210"
    assert form.get_output_subject() == "Computer Science"
    assert form.get_output_currentAddr() == "Nepal"

    time.sleep(5)
    # Close
    driver.quit()
