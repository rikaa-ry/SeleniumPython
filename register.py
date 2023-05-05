import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from data import dataInput
from baseRegister import registerUser

class Register(unittest.TestCase):

    webURL = dataInput.baseURL + "register"

    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    # Positive Test Cases
    def test_succes_register(self):
        driver = self.driver
        registerUser(driver, dataInput.genderFemale, dataInput.firstName, dataInput.lastName, dataInput.random_email, dataInput.valid_pass)
        url = driver.current_url
        self.assertEqual(url, dataInput.baseURL + "registerresult/1")
        results = driver.find_elements(By.CLASS_NAME, "result")
        for result in results:
            text = result.text
        self.assertIn("Your registration completed", text)

    def test_failed_register_empty_all_field(self):
        driver = self.driver
        driver.get(self.webURL)
        driver.find_element(By.ID, "register-button").click()
        firstName = driver.find_element(By.CSS_SELECTOR, "[data-valmsg-for=FirstName]").text
        lastName = driver.find_element(By.CSS_SELECTOR, "[data-valmsg-for=LastName]").text
        email = driver.find_element(By.CSS_SELECTOR, "[data-valmsg-for=Email]").text
        password = driver.find_element(By.CSS_SELECTOR, "[data-valmsg-for=Password]").text
        confirmPassword = driver.find_element(By.CSS_SELECTOR, "[data-valmsg-for=ConfirmPassword]").text
        self.assertIn("First name is required.", firstName)
        self.assertIn("Last name is required.", lastName)
        self.assertIn("Email is required.", email)
        self.assertIn("Password is required.", password)
        self.assertIn("Password is required.", confirmPassword)

    def test_failed_register_weak_password(self):
        driver = self.driver
        registerUser(driver, dataInput.genderMale, dataInput.firstName, dataInput.lastName, dataInput.random_email, "abc")
        data = driver.find_element(By.CSS_SELECTOR, "[data-valmsg-for=Password]").text
        self.assertIn("The password should have at least 6 characters.", data)

    def test_failed_register_email_exist(self):
        driver = self.driver
        registerUser(driver, dataInput.genderFemale, dataInput.firstName, dataInput.lastName, dataInput.valid_email, dataInput.valid_pass)
        errors = driver.find_elements(By.CLASS_NAME, "validation-summary-errors > ul")
        for error in errors:
            text = error.text
        self.assertIn("The specified email already exists", text)

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()