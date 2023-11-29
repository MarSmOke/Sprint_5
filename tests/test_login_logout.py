from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
import locators


def test_login_account_main_button(login_check):
    driver = login_check
    driver.get(locators.main_url)
    driver.find_element(By.XPATH, locators.login_into_account_button).click()


def test_login_lk_button(login_check):
    driver = login_check
    driver.get(locators.main_url)
    driver.find_element(By.CSS_SELECTOR, locators.lk_button).click()


def test_login_registration_button(login_check):
    driver = login_check
    driver.get(locators.registration_url)
    driver.find_element(By.CSS_SELECTOR, locators.login_button_side).click()


def test_login_password_restore_button(login_check):
    driver = login_check
    driver.get(locators.forgot_password_url)
    driver.find_element(By.CSS_SELECTOR, locators.login_button_side).click()


def test_logout(login_main):
    driver = login_main
    driver.find_element(By.CSS_SELECTOR, locators.lk_button).click()
    WebDriverWait(driver, 3).until(
        expected_conditions.visibility_of_element_located(
            (By.XPATH, locators.lk_text)))
    driver.find_element(By.XPATH, locators.logout_button).click()
    WebDriverWait(driver, 3).until(
        expected_conditions.visibility_of_element_located((By.XPATH, locators.login_button_main)))
    assert driver.current_url == locators.login_url

