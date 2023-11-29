from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
import locators


def test_go_to_lk(login_main):
    driver = login_main
    driver.find_element(By.CSS_SELECTOR, locators.lk_button).click()
    WebDriverWait(driver, 3).until(
        expected_conditions.visibility_of_element_located((By.XPATH, locators.lk_text)))
    assert driver.current_url == locators.lk_url


def test_go_to_constructor(login_main):
    driver = login_main
    driver.find_element(By.CSS_SELECTOR, locators.lk_button).click()
    WebDriverWait(driver, 3).until(
        expected_conditions.visibility_of_element_located(
            (By.XPATH, locators.lk_text)))
    driver.find_element(By.XPATH, locators.constructor_button).click()
    WebDriverWait(driver, 3).until(
        expected_conditions.visibility_of_element_located((By.XPATH, locators.main_paragraph)))
    assert driver.current_url == locators.main_url


def test_go_to_logo(login_main):
    driver = login_main
    driver.find_element(By.CSS_SELECTOR, locators.lk_button).click()
    WebDriverWait(driver, 3).until(
        expected_conditions.visibility_of_element_located(
            (By.XPATH, locators.lk_text)))
    driver.find_element(By.XPATH, locators.logo).click()
    WebDriverWait(driver, 3).until(
        expected_conditions.visibility_of_element_located((By.XPATH, locators.main_paragraph)))
    assert driver.current_url == locators.main_url
