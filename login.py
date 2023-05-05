import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from baseLogin import doLogin
from data import dataInput

class Login(unittest.TestCase):

    webURL = dataInput.baseURL + "login"

    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    # Positive Test Cases
    def test_succes_login(self):
        driver = self.driver
        doLogin(driver, dataInput.valid_email, dataInput.valid_pass)
        self.assertEqual(dataInput.baseURL, dataInput.baseURL)
        results = driver.find_elements(By.CLASS_NAME, "account")
        for result in results:
            text = result.text
            break
        self.assertIn("rika11@gmail.com", text)

    def test_failed_login_empty_all_field(self):
        driver = self.driver
        driver.get(self.webURL)
        driver.find_element(By.CLASS_NAME, "login-button").click()
        error = driver.find_element(By.CLASS_NAME, "validation-summary-errors").text
        self.assertIn("Login was unsuccessful. Please correct the errors and try again.", error)
        self.assertIn("No customer account found", error)

    def test_failed_login_wrong_password(self):
        driver = self.driver
        doLogin(driver, dataInput.valid_email, dataInput.invalid_pass)
        error = driver.find_element(By.CLASS_NAME, "validation-summary-errors").text
        self.assertIn("Login was unsuccessful. Please correct the errors and try again.", error)
        self.assertIn("The credentials provided are incorrect", error)

    def test_failed_login_not_a_customer(self):
        driver = self.driver
        doLogin(driver, dataInput.not_a_user, dataInput.invalid_pass)
        error = driver.find_element(By.CLASS_NAME, "validation-summary-errors").text
        self.assertIn("Login was unsuccessful. Please correct the errors and try again.", error)
        self.assertIn("No customer account found", error)

    def test_failed_login_invalid_email(self):
        driver = self.driver
        doLogin(driver, dataInput.invalid_user, dataInput.invalid_pass)
        error = driver.find_element(By.CLASS_NAME, "field-validation-error").text
        self.assertIn("Please enter a valid email address.", error)

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()