from pages.dashboard_pages import DashboardPages
from pages.login_pages import LoginPage
import allure

@allure.story("Login Feature")
@allure.description("Verify that a user can login successfully with valid credentials")
def test_login(driver):

    login = LoginPage(driver)
    dashboard = DashboardPages(driver)

    with allure.step("Enter company ID"):
        login.enter_company_id("5049209")
    with allure.step("Enter username"):
        login.enter_username("qatestsalesman")

    with allure.step("Enter password"):
        login.enter_password("it.QA2025")

    with allure.step("Tap login button"):
        login.tap_login()
    
    with allure.step("Verify that eWork text is displayed on dashboard"):
        assert dashboard.is_ework_text_displayed(), "eWork text is not displayed on dashboard"

