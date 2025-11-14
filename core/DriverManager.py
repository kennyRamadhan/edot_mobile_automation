import threading

class DriverManager:
    _driver_local = threading.local()

    @staticmethod
    def set_driver(driver):
        DriverManager._driver_local.driver = driver

    @staticmethod
    def get_driver():
        return getattr(DriverManager._driver_local, "driver", None)

    @staticmethod
    def unload():
        DriverManager._driver_local.driver = None
