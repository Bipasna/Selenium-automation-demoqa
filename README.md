# Selenium Automation - DemoQA 

This is a practice Selenium automation project for the [DemoQA](https://demoqa.com/automation-practice-form) website.

---

## 📁 Project Structure
S_Demoqa/
│
├── tests/ # Test scripts
├── pages/ # Page Object Model files
├── drivers/ # WebDriver executables
├── images/ # Test image uploads
├── utils/ # Utility files (if any)
└── README.md

---

## 🧰 Dependencies

This project uses the following tools and libraries:

- Python 3.11.3
- [Selenium](https://pypi.org/project/selenium/)
- [PyTest](https://pypi.org/project/pytest/)
- [Allure-pytest (optional for reporting)](https://pypi.org/project/allure-pytest/)
- [WebDriver Manager (optional)](https://pypi.org/project/webdriver-manager/) *(if not using manual drivers)*

Install them using pip:

```bash
pip install -r requirements.txt

Or manually:

In bash
pip install selenium pytest allure-pytest


HOW TO RUN THE TESTS
pytest -s tests/FormTest/form_test.py
