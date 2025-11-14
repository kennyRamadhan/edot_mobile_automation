from appium.webdriver.common.appiumby import AppiumBy
from core.base_page import BasePage

class LoginPage(BasePage):

    COMPANY_ID_FIELD = (AppiumBy.ID, "id.edot.ework:id/tv_company_id")
    USERNAME_FIELD = (AppiumBy.ID, "id.edot.ework:id/tv_username")
    PASSWORD_FIELD   = (AppiumBy.ID, "id.edot.ework:id/tv_password")
    LOGIN_BUTTON   = (AppiumBy.ID, "id.edot.ework:id/button_text")

    def enter_company_id(self, company_id):
        self.type(self.COMPANY_ID_FIELD, company_id)
    
    def enter_username(self, username):
        self.type(self.USERNAME_FIELD, username)

    def enter_password(self, password):
        self.type(self.PASSWORD_FIELD, password)

    def tap_login(self):
        self.click(self.LOGIN_BUTTON)
