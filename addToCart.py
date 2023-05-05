import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from baseLogin import doLogin
from data import dataInput

class addToCart(unittest.TestCase):

    webURL = dataInput.baseURL + "25-virtual-gift-card"

    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    # Positive Test Cases
    def test_succes_add_to_cart(self):
        driver = self.driver
        doLogin(driver, dataInput.valid_email, dataInput.valid_pass)
        driver.get(self.webURL)
        driver.find_element(By.ID, "giftcard_2_RecipientName").send_keys("Rika")
        driver.find_element(By.ID, "giftcard_2_RecipientEmail").send_keys("rika11@gmail.com")
        driver.find_element(By.ID, "add-to-cart-button-2").click()
        qty = driver.find_element(By.CLASS_NAME, "cart-qty").text
        alerts = driver.find_elements(By.CLASS_NAME, 'bar-notification')
        for alert in alerts:
            text = alert.text
            print(text)
        assert qty != '(0)'
        self.assertIn("The product has been added to your shopping cart", text)

    def test_failed_add_to_cart_empty_field_recipient_name(self):
        driver = self.driver
        doLogin(driver, dataInput.valid_email, dataInput.valid_pass)
        driver.get(self.webURL)
        driver.find_element(By.ID, "giftcard_2_RecipientEmail").send_keys("rika11@gmail.com")
        driver.find_element(By.ID, "add-to-cart-button-2").click()
        alerts = driver.find_elements(By.CLASS_NAME, 'bar-notification')
        for alert in alerts:
            text = alert.text
            print(text)
        self.assertIn("Enter valid recipient name", text)

    def test_failed_add_to_cart_empty_field_recipient_email(self):
        driver = self.driver
        doLogin(driver, dataInput.valid_email, dataInput.valid_pass)
        driver.get(self.webURL)
        driver.find_element(By.ID, "giftcard_2_RecipientName").send_keys("Rika")
        driver.find_element(By.ID, "add-to-cart-button-2").click()
        alerts = driver.find_elements(By.CLASS_NAME, 'bar-notification')
        for alert in alerts:
            text = alert.text
            print(text)
        self.assertIn("Enter valid recipient email", text)

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()