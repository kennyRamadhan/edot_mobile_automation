from pages.login_pages import LoginPage


def test_login(driver):

    login = LoginPage(driver)
    login.enter_company_id("5049209")  
    login.enter_username("qatestsalesman")    
    login.enter_password("it.QA2025")
    login.tap_login()
