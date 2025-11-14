from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

class BasePage:

    def __init__(self, driver, timeout=10):
        self.driver = driver
        self.timeout = timeout  # default wait 10 detik

    def find(self, locator):
        """Find element with explicit wait until it is present"""
        try:
            return WebDriverWait(self.driver, self.timeout).until(
                EC.presence_of_element_located(locator)
            )
        except TimeoutException:
            raise Exception(f"Element {locator} not found after {self.timeout} seconds")

    def click(self, locator):
        el = self.find(locator)
        WebDriverWait(self.driver, self.timeout).until(
            EC.element_to_be_clickable(locator)
        )
        el.click()

    def type(self, locator, text):
        el = self.find(locator)
        WebDriverWait(self.driver, self.timeout).until(
            EC.visibility_of(el)
        )
        el.clear()
        el.send_keys(text)

    def get_text(self, locator):
        el = self.find(locator)
        return el.text

    def scroll_down(self):
        size = self.driver.get_window_size()
        start_y = size["height"] * 0.8
        end_y = size["height"] * 0.2
        x = size["width"] * 0.5

        self.driver.swipe(x, start_y, x, end_y, 500)
