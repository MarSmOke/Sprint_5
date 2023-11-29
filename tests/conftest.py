import random
import pytest
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions


@pytest.fixture
def credentials():
    name = 'Marina'
    email = f"marinasmirnova3{random.randint(1, 999)}@ya.ru"
    password = f'{random.randint(100000, 999000)}'
    return name, email, password


@pytest.fixture
def login_main():
    driver = webdriver.Chrome()
    driver.get("https://stellarburgers.nomoreparties.site/login")
    driver.find_element(By.XPATH, ".//fieldset[1]//input").send_keys('r.aters@ya.ru')
    driver.find_element(By.XPATH, ".//fieldset[2]//input").send_keys('sVUsnk9WRwxUH2Z')
    driver.find_element(By.XPATH, ".//button[text()='Войти']").click()
    WebDriverWait(driver, 3).until(
        expected_conditions.visibility_of_element_located((By.XPATH, ".//section/h1[text()='Соберите бургер']")))
    yield driver
    driver.quit()


@pytest.fixture
def login_check():
    driver = webdriver.Chrome()
    yield driver
    driver.find_element(By.XPATH, ".//fieldset[1]//input").send_keys('r.aters@ya.ru')
    driver.find_element(By.XPATH, ".//fieldset[2]//input").send_keys('sVUsnk9WRwxUH2Z')
    driver.find_element(By.XPATH, ".//button[text()='Войти']").click()
    WebDriverWait(driver, 3).until(
        expected_conditions.visibility_of_element_located((By.XPATH, ".//section/h1[text()='Соберите бургер']")))
    assert driver.current_url == 'https://stellarburgers.nomoreparties.site/'
    driver.quit()
