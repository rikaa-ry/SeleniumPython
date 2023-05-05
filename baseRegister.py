from selenium.webdriver.common.by import By
from data import dataInput

def registerUser(driver, gender, firstName, lastName, email, password):
    driver.get(dataInput.baseURL+"register")
    driver.find_element(By.ID, gender).click()
    driver.find_element(By.ID, "FirstName").send_keys(firstName)
    driver.find_element(By.ID, "LastName").send_keys(lastName)
    driver.find_element(By.ID, "Email").send_keys(email)
    driver.find_element(By.ID, "Password").send_keys(password)
    driver.find_element(By.ID, "ConfirmPassword").send_keys(password)
    driver.find_element(By.ID, "register-button").click()