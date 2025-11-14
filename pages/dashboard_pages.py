from appium.webdriver.common.appiumby import AppiumBy
from core.base_page import BasePage

class DashboardPages(BasePage):

    EWORK_TEXT = (AppiumBy.ID, "id.edot.ework:id/img_ework")
   

    def is_ework_text_displayed(self):
        return self.find(self.EWORK_TEXT).is_displayed()

