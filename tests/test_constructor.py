from selenium.webdriver.common.by import By
import locators


class TestNavigation:
    def test_buns_is_default_tab(self, setup_driver):
        driver = setup_driver
        driver.get(locators.main_url)
        driver.find_element(By.XPATH, locators.sauces_tab).click()
        driver.find_element(By.XPATH, locators.buns_tab).click()
        assert locators.selected_tab in driver.find_element(By.XPATH, locators.buns_main_tab).get_attribute('class')

    def test_go_to_sauces(self, setup_driver):
        driver = setup_driver
        driver.get(locators.main_url)
        driver.find_element(By.XPATH, locators.sauces_tab).click()
        assert locators.selected_tab in driver.find_element(By.XPATH, locators.sauces_main_tab).get_attribute('class')

    def test_go_to_fillings(self, setup_driver):
        driver = setup_driver
        driver.get(locators.main_url)
        driver.find_element(By.XPATH, locators.fillings_tab).click()
        assert locators.selected_tab in driver.find_element(By.XPATH, locators.fillings_main_tab).get_attribute('class')
