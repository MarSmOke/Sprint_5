from selenium.webdriver.common.by import By
from selenium import webdriver
import locators


def test_buns_is_default_tab():
    driver = webdriver.Chrome()
    driver.get(locators.main_url)
    assert driver.find_element(By.XPATH, locators.buns_main_tab).text == 'Булки'
    driver.quit()


def test_go_to_sauces():
    driver = webdriver.Chrome()
    driver.get(locators.main_url)
    driver.find_element(By.XPATH, locators.sauces_tab).click()
    assert driver.find_element(By.XPATH, locators.sauces_main_tab).text == 'Соусы'
    driver.quit()


def test_go_to_fillings():
    driver = webdriver.Chrome()
    driver.get(locators.main_url)
    driver.find_element(By.XPATH, locators.fillings_tab).click()
    assert driver.find_element(By.XPATH, locators.fillings_main_tab).text == 'Начинки'
    driver.quit()
