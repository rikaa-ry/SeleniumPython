import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from baseLogin import doLogin
from data import dataInput

class Checkout(unittest.TestCase):

    webURL = dataInput.baseURL + "cart"

    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    # Positive Test Cases
    def test_succes_checkout(self):
        driver = self.driver
        doLogin(driver, dataInput.valid_email, dataInput.valid_pass)
        driver.get(self.webURL)
        driver.find_element(By.ID, "termsofservice").click()
        driver.find_element(By.ID, "checkout").click()
        url = driver.current_url
        self.assertEqual(url, dataInput.baseURL + "onepagecheckout")

    def test_failed_checkout(self):
        driver = self.driver
        doLogin(driver, dataInput.valid_email, dataInput.valid_pass)
        driver.get(self.webURL)
        driver.find_element(By.ID, "checkout").click()
        warning = driver.find_element(By.ID, "terms-of-service-warning-box").text
        self.assertIn("Please accept the terms of service before the next step.", warning)

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()