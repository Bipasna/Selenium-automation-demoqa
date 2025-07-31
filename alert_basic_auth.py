from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time



# Set Path to ChromeDriver if not in PATH
service =  Service(executable_path="E:\\S_Demoqa\\drivers\\chromedriver-win64\\chromedriver.exe")

# Step 1: Launch browser
driver= webdriver.Chrome(service=service)


# BASIC AUTH POPUP
# Step 2: Pass credentials in URL
basic_auth_url= "https://matat:coffee9191@stg.coffeeshop51.com/"
driver.get(basic_auth_url)

# Step 3: Get and print page title
title = driver.title
print("Page Title:", title)

#Step 4: Verify success based on title
expected_title = "דף הבית - קפה 51 - בית קלייה מקומי לקפה ספיישלטי - חמישים ואחד - Coffee Shop 51"
if expected_title in title:
    print("Login success")
else:
    print("Login failed")

# Step 4: Wait and close
time.sleep(3)



#JAVASCRIPT ALERT POPUP

driver.get("https://demoqa.com/alerts")
time.sleep(2)

#click button to trigger alert
driver.find_element(By.ID, "alertButton").click()
time.sleep(1)

#switch to alert and accept
alert = driver.switch_to.alert
print("Alert Text:", alert.text)
alert.accept()
print("JS Alert accepted.")


#HTML MODAL POPUP
driver.get("https://demoqa.com/modal-dialogs")
time.sleep(2)

#open small modal
driver.find_element(By.ID, "showSmallModal").click()
time.sleep(1)

# Get modal title text
modal_title = driver.find_element(By.ID, "example-modal-sizes-title-sm").text
print("Modal Title:", modal_title)

# Close modal
driver.find_element(By.ID, "closeSmallModal").click()
print("HTML modal handled.")

driver.quit()


#(venv)E:\S_Demoqa>python alert_basic_auth.py


