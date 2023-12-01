import random
import pytest
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
import locators


@pytest.fixture
def setup_driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()


@pytest.fixture
def credentials():
    name = 'Marina'
    email = f"marinasmirnova3{random.randint(1, 999)}@ya.ru"
    password = f'{random.randint(100000, 999000)}'
    return name, email, password


@pytest.fixture
def login_main(setup_driver):
    driver = setup_driver
    driver.get(locators.login_url)
    driver.find_element(By.XPATH, locators.email).send_keys('r.aters@ya.ru')
    driver.find_element(By.XPATH, locators.password).send_keys('sVUsnk9WRwxUH2Z')
    driver.find_element(By.XPATH, locators.login_button_main).click()
    WebDriverWait(driver, 3).until(
        expected_conditions.visibility_of_element_located((By.XPATH, locators.main_paragraph)))
    yield driver

