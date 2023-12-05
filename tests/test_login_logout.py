from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
import locators


class TestLogs:
    def test_login_account_main_button(self, setup_driver):
        driver = setup_driver
        driver.get(locators.main_url)
        driver.find_element(By.XPATH, locators.login_into_account_button).click()
        driver.find_element(By.XPATH, locators.email).send_keys('r.aters@ya.ru')
        driver.find_element(By.XPATH, locators.password).send_keys('sVUsnk9WRwxUH2Z')
        driver.find_element(By.XPATH, locators.login_button_main).click()
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located((By.XPATH, locators.main_paragraph)))
        assert driver.current_url == 'https://stellarburgers.nomoreparties.site/'

    def test_login_lk_button(self, setup_driver):
        driver = setup_driver
        driver.get(locators.main_url)
        driver.find_element(By.CSS_SELECTOR, locators.lk_button).click()
        driver.find_element(By.XPATH, locators.email).send_keys('r.aters@ya.ru')
        driver.find_element(By.XPATH, locators.password).send_keys('sVUsnk9WRwxUH2Z')
        driver.find_element(By.XPATH, locators.login_button_main).click()
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located((By.XPATH, locators.main_paragraph)))
        assert driver.current_url == 'https://stellarburgers.nomoreparties.site/'

    def test_login_registration_button(self, setup_driver):
        driver = setup_driver
        driver.get(locators.registration_url)
        driver.find_element(By.CSS_SELECTOR, locators.login_button_side).click()
        driver.find_element(By.XPATH, locators.email).send_keys('r.aters@ya.ru')
        driver.find_element(By.XPATH, locators.password).send_keys('sVUsnk9WRwxUH2Z')
        driver.find_element(By.XPATH, locators.login_button_main).click()
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located((By.XPATH, locators.main_paragraph)))
        assert driver.current_url == 'https://stellarburgers.nomoreparties.site/'

    def test_login_password_restore_button(self, setup_driver):
        driver = setup_driver
        driver.get(locators.forgot_password_url)
        driver.find_element(By.CSS_SELECTOR, locators.login_button_side).click()
        driver.find_element(By.XPATH, locators.email).send_keys('r.aters@ya.ru')
        driver.find_element(By.XPATH, locators.password).send_keys('sVUsnk9WRwxUH2Z')
        driver.find_element(By.XPATH, locators.login_button_main).click()
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located((By.XPATH, locators.main_paragraph)))
        assert driver.current_url == 'https://stellarburgers.nomoreparties.site/'

    def test_logout(self, login_main):
        driver = login_main
        driver.find_element(By.CSS_SELECTOR, locators.lk_button).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(
            (By.XPATH, locators.lk_text)))
        driver.find_element(By.XPATH, locators.logout_button).click()
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located((By.XPATH, locators.login_button_main)))
        assert driver.current_url == locators.login_url

