from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
import locators


class TestRegistration:
    def test_registration_successful(self, credentials, setup_driver):
        driver = setup_driver
        driver.get(locators.registration_url)
        driver.find_element(By.XPATH, locators.name).send_keys(credentials[0])
        driver.find_element(By.XPATH, locators.email).send_keys(credentials[1])
        driver.find_element(By.XPATH, locators.password).send_keys(credentials[2])
        driver.find_element(By.XPATH, locators.registration_button).click()
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located((By.XPATH, locators.login_button_main)))
        assert driver.current_url == locators.login_url

    def test_registration_incorrect_password(self, credentials, setup_driver):
        driver = setup_driver
        driver.get(locators.registration_url)
        driver.find_element(By.XPATH, locators.name).send_keys(credentials[0])
        driver.find_element(By.XPATH, locators.email).send_keys(credentials[1])
        driver.find_element(By.XPATH, locators.password).send_keys('123')
        driver.find_element(By.XPATH, locators.registration_button).click()
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located((By.XPATH, locators.password_error)))
        error = driver.find_element(By.XPATH, locators.password_error)
        assert error.text == 'Некорректный пароль'
        