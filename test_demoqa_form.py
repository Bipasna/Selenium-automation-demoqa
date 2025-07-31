from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

# Set path to ChromeDriver using Service object
service = Service("E:\\S_Demoqa\\drivers\\chromedriver-win64\\chromedriver.exe")

# Create driver
driver = webdriver.Chrome(service=service)
driver.maximize_window()

# Open DemoQA Text Box page
driver.get("https://demoqa.com/text-box")

# Fill in form
driver.find_element(By.ID, "userName").send_keys("Bipashna Maharzan")
driver.find_element(By.ID, "userEmail").send_keys("bipashna@example.com")
driver.find_element(By.ID, "currentAddress").send_keys("Lalitpur")
driver.find_element(By.ID, "permanentAddress").send_keys("Kathmandu")

# Submit form
driver.find_element(By.ID, "submit").click()

# Wait and fetch results
time.sleep(2)
print(driver.find_element(By.ID, "name").text)
print(driver.find_element(By.ID, "email").text)

# Close browser
driver.quit()


#(venv)E:\S_Demoqa>python test_demaqa_form.py

