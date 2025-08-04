from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select



class FormPage:
    def __init__(self, driver):
        self.driver = driver

        # Locators
        self.firstname_input = (By.ID, "firstName")
        self.lastname_input = (By.ID, "lastName")
        self.email_input = (By.ID, "userEmail")

        # Locator for the clickable label
        self.gender_male = (By.XPATH, "//label[@for='gender-radio-1']")
        self.mobile_input = (By.ID, "userNumber")
        self.dob_input = (By.ID, "dateOfBirthInput")
        self.subject_input = (By.ID,"subjectsInput")

        self.hobby_sports_checkbox = (By.XPATH, "//label[@for='hobbies-checkbox-1']")
        self.hobby_reading_checkbox = (By.XPATH, "//label[@for='hobbies-checkbox-2']")
        self.hobby_music_checkbox = (By.XPATH, "//label[@for='hobbies-checkbox-3']")

        self.upload_input =(By.ID, "uploadPicture")
        self.Addr_input = (By.ID, "currentAddress")

        self.state_dropdown = (By.ID, "state")
        self.city_dropdown = (By.ID, "city")

        self.submit_button = (By.ID, "submit")


        self.fullname_output = (By.XPATH, "//td[text()='Student Name']/following-sibling::td")
        self.output_email = (By.XPATH, "//td[text()='Student Email']/following-sibling::td")
        self.output_gender = (By.XPATH, "//td[text()='Gender']/following-sibling::td")
        self.output_mobile = (By.XPATH, "//td[text()='Mobile']/following-sibling::td")
        self.output_dob = (By.XPATH, "//td[text()='Date of Birth']/following-sibling::td")
        self.output_subject = (By.XPATH, "//td[text()='Subjects']/following-sibling::td")
        self.output_currentAddr = (By.XPATH, "//td[text()='Address']/following-sibling::td")


    # Actions
    def open(self):
        self.driver.get("https://demoqa.com/automation-practice-form")

    def fill_form(self, firstname, lastname, email, subject, currentAddr):
        self.driver.find_element(*self.firstname_input).send_keys(firstname)
        self.driver.find_element(*self.lastname_input).send_keys(lastname)
        self.driver.find_element(*self.email_input).send_keys(email)

        # Type subject and when handle dropdown individually
        subject_input = self.driver.find_element(*self.subject_input)
        subject_input.send_keys(subject)
    
        # Wait for suggestion dropdown to appear and press DOWN + ENTER
        WebDriverWait(self.driver, 5).until(
        EC.visibility_of_element_located((By.ID, "react-select-2-option-0"))
        )
        subject_input.send_keys(Keys.ARROW_DOWN)
        subject_input.send_keys(Keys.ENTER)


        self.driver.find_element(*self.Addr_input).send_keys(currentAddr)
        
    def select_hobbies(self, *hobbies):
        for hobby in hobbies:
            if hobby.lower() == "sports":
                self.driver.find_element(*self.hobby_sports_checkbox).click()
            elif hobby.lower() == "music":
                self.driver.find_element(*self.hobby_music_checkbox).click()
            elif hobby.lower() == "reading":
                self.driver.find_element(*self.hobby_reading_checkbox).click()

        
    def select_gender_male(self):
        self.driver.find_element(*self.gender_male).click()

    def select_mobile(self, mobile):
        self.driver.find_element(*self.mobile_input).send_keys(mobile)

    def select_dob(self, day: str, month: str, year: str):
        self.driver.find_element(By.ID, "dateOfBirthInput").click()

     # Select year
        year_dropdown = Select(self.driver.find_element(By.CLASS_NAME, "react-datepicker__year-select"))
        year_dropdown.select_by_visible_text(year)

    # Select month
        month_dropdown = Select(self.driver.find_element(By.CLASS_NAME, "react-datepicker__month-select"))
        month_dropdown.select_by_visible_text(month)

    # Select day (remove leading zeros if needed)
        day_selector = f"//div[contains(@class, 'react-datepicker__day') and text()='{int(day)}']"
        self.driver.find_element(By.XPATH, day_selector).click()

    def upload_picture(self, file_path):
        self.driver.find_element(*self.upload_input).send_keys(file_path)
    

    def select_state(self, state_name):
        state_dropdown = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.state_dropdown)
        )

    # Scroll into view with JS (more reliable than ActionChains for dropdowns)
        self.driver.execute_script("arguments[0].scrollIntoView(true);", state_dropdown)
        state_dropdown.click()

        option_xpath = f"//div[contains(@id, 'react-select-3-option') and text()='{state_name}']"
        option = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, option_xpath))
        )
        self.driver.execute_script("arguments[0].scrollIntoView(true);", option)
        option.click()




    def select_city(self, city_name):
        city_dropdown = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.city_dropdown)
        )
    
        self.driver.execute_script("arguments[0].scrollIntoView(true);", city_dropdown)
        city_dropdown.click()

        option_xpath = f"//div[contains(@id, 'react-select-4-option') and text()='{city_name}']"
        city_option = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, option_xpath))
        )
        self.driver.execute_script("arguments[0].scrollIntoView(true);", city_option)
        city_option.click()



    def submit(self):
        submit_button = self.driver.find_element(*self.submit_button)
        self.driver.execute_script("arguments[0].scrollIntoView(true);", submit_button)
        submit_button.click()


    def get_output_fullname(self):
        WebDriverWait(self.driver, 10).until(
        EC.visibility_of_element_located(self.fullname_output)
        )
        return self.driver.find_element(*self.fullname_output).text.strip()



    def get_output_email(self):
        return self.driver.find_element(*self.output_email).text
    
    def get_output_gender(self):
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.output_gender)
        )
        return self.driver.find_element(*self.output_gender).text.strip()

    def get_output_mobile(self):
        return self.driver.find_element(*self.output_mobile).text
    
    def get_output_dob(self):
        return self.driver.find_element(*self.output_dob).text
    
    def get_output_subject(self):
        return self.driver.find_element(*self.output_subject).text
    
    def get_output_currentAddr(self):
        return self.driver.find_element(*self.output_currentAddr).text