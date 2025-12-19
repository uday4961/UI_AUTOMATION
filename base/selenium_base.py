from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select


class SeleniumBase:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 15)

    def click(self, locator):
        self.wait.until(EC.element_to_be_clickable(locator)).click()

    def send_keys(self, locator, text):
        elem = self.wait.until(EC.visibility_of_element_located(locator))
        elem.clear()
        elem.send_keys(text)

    def select_by_visible_text(self, locator, text):
        dropdown = self.wait.until(EC.element_to_be_clickable(locator))
        Select(dropdown).select_by_visible_text(text)

    def get_text(self, locator):
        return self.wait.until(EC.visibility_of_element_located(locator)).text

    def select_by_text(self, locator, visible_text):
        dropdown = self.wait.until(EC.presence_of_element_located(locator))
        Select(dropdown).select_by_visible_text(visible_text)

    def select_radio(self, locator):
        element = self.wait.until(EC.element_to_be_clickable(locator))
        if not element.is_selected():
            element.click()