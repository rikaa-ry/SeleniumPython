from selenium.webdriver.common.by import By
from data import dataInput

def doLogin(driver, email, password):
    driver.get(dataInput.baseURL+"login")
    driver.find_element(By.ID, "Email").send_keys(email)
    driver.find_element(By.ID, "Password").send_keys(password)
    driver.find_element(By.CLASS_NAME, "login-button").click()