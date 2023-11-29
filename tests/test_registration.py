from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
import locators


def test_registration_successful(credentials):
    driver = webdriver.Chrome()
    driver.get(locators.registration_url)
    driver.find_element(By.XPATH, locators.name).send_keys(credentials[0])
    driver.find_element(By.XPATH, locators.email).send_keys(credentials[1])
    driver.find_element(By.XPATH, locators.password).send_keys(credentials[2])
    driver.find_element(By.XPATH, locators.registration_button).click()
    WebDriverWait(driver, 3).until(
        expected_conditions.visibility_of_element_located((By.XPATH, locators.login_button_main)))
    assert driver.current_url == locators.login_url
    driver.quit()


def test_registration_incorrect_password(credentials):
    driver = webdriver.Chrome()
    driver.get(locators.registration_url)
    driver.find_element(By.XPATH, locators.name).send_keys(credentials[0])
    driver.find_element(By.XPATH, locators.email).send_keys(credentials[1])
    driver.find_element(By.XPATH, locators.password).send_keys('123')
    driver.find_element(By.XPATH, locators.registration_button).click()
    WebDriverWait(driver, 3).until(
        expected_conditions.visibility_of_element_located((By.XPATH, locators.password_error)))
    error = driver.find_element(By.XPATH, locators.password_error)
    assert error.text == 'Некорректный пароль'
    driver.quit()



