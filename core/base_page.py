from appium.webdriver.common.appiumby import AppiumBy

class BasePage:

    def __init__(self, driver):
        self.driver = driver

    def find(self, locator):
        return self.driver.find_element(*locator)

    def click(self, locator):
        self.find(locator).click()

    def type(self, locator, text):
        el = self.find(locator)
        el.clear()
        el.send_keys(text)

    def get_text(self, locator):
        return self.find(locator).text

    def scroll_down(self):
        size = self.driver.get_window_size()
        start_y = size["height"] * 0.8
        end_y = size["height"] * 0.2
        x = size["width"] * 0.5

        self.driver.swipe(x, start_y, x, end_y, 500)
