from selenium.webdriver.common.by import By

class TextBoxPage:
    def __init__(self, driver):
        self.driver = driver

        # Locators
        self.username_input = (By.ID, "userName")
        self.email_input = (By.ID, "userEmail")
        self.current_address_input = (By.ID, "currentAddress")
        self.permanent_address_input = (By.ID, "permanentAddress")
        self.submit_button = (By.ID, "submit")

        self.output_name = (By.ID, "name")
        self.output_email = (By.ID, "email")

    # Actions
    def open(self):
        self.driver.get("https://demoqa.com/text-box")

    def fill_form(self, name, email, current_address, permanent_address):
        self.driver.find_element(*self.username_input).send_keys(name)
        self.driver.find_element(*self.email_input).send_keys(email)
        self.driver.find_element(*self.current_address_input).send_keys(current_address)
        self.driver.find_element(*self.permanent_address_input).send_keys(permanent_address)

    def submit(self):
        self.driver.find_element(*self.submit_button).click()

    def get_output_name(self):
        return self.driver.find_element(*self.output_name).text

    def get_output_email(self):
        return self.driver.find_element(*self.output_email).text
