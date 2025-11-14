from core.appium_server_manager import AppiumServerManager
from core.DriverManager import DriverManager
import pytest
import allure


def pytest_addoption(parser):
    parser.addoption("--device", action="store", default="android")


@pytest.fixture(scope="session", autouse=True)
def appium_server():
    port = AppiumServerManager.start_server()
    yield
    AppiumServerManager.stop_server()


@pytest.fixture(scope="session")
def driver(request):
    device = request.config.getoption("--device")

    caps_path = (
        "config/capabilities_android.json"
        if device == "android"
        else "config/capabilities_ios.json"
    )

    drv = AppiumServerManager.init_driver(caps_path)
    DriverManager.set_driver(drv)

    yield drv

    allure.attach(
        drv.get_screenshot_as_png(),
        name="final_screenshot",
        attachment_type=allure.attachment_type.PNG,
    )

    drv.quit()
    DriverManager.unload()
