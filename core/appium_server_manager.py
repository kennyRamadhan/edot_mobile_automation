import os
import random
import subprocess
from appium import webdriver
from time import sleep
import json
from appium.options.android import UiAutomator2Options
from appium.options.ios import XCUITestOptions
import requests

class AppiumServerManager:
    _server_process = None
    _driver = None
    _port = None

    @staticmethod
    def _find_node():
        guesses = [
            "/opt/homebrew/bin/node",
            "/usr/local/bin/node",
            os.path.expanduser("~/.nvm/versions/node/current/bin/node"),
            "/usr/bin/node"
        ]
        for path in guesses:
            if os.path.exists(path):
                return path
        raise FileNotFoundError("Node.js not found!")

    @staticmethod
    def _find_appium_main_js():
        guesses = [
            os.path.expanduser("~/.appium/node_modules/appium/build/lib/main.js"),
            "/usr/local/lib/node_modules/appium/build/lib/main.js",
            "/opt/homebrew/lib/node_modules/appium/build/lib/main.js",
        ]
        for path in guesses:
            if os.path.exists(path):
                return path
        raise FileNotFoundError("Appium main.js not found!")

    @staticmethod
    def start_server():
        port = 4723
        print(f"🚀 Starting Appium on port {port}")

        AppiumServerManager._server_process = subprocess.Popen(
            ["appium", "-p", str(port)],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )

        AppiumServerManager._port = port
        
        # --- NEW CODE: Robust check for server readiness ---
        url = f"http://127.0.0.1:{port}/status" 
        max_retries = 10
        for i in range(max_retries):
            try:
                # Check for Appium server status endpoint
                response = requests.get(url, timeout=1) 
                if response.status_code == 200:
                    print("✅ Appium server is running and ready.")
                    break
            except requests.exceptions.ConnectionError:
                pass # Server not ready yet

            if i < max_retries - 1:
                sleep(1) # Wait 1 second before retrying
            else:
                raise Exception("Appium server failed to start within the timeout.")
        # --- END NEW CODE ---
        
        return port
    @staticmethod
    def stop_server():
        if AppiumServerManager._server_process:
            AppiumServerManager._server_process.terminate()
            print("🛑 Appium server stopped")

    @staticmethod
    def init_driver(caps_path):
        with open(caps_path) as f:
            caps = json.load(f)

        # 🔥 Gunakan port yang sama dengan start_server()
        url = f"http://127.0.0.1:{AppiumServerManager._port}"

        platform = caps.get("platformName", "").lower()

        if platform == "android":
            options = UiAutomator2Options().load_capabilities(caps)
        elif platform == "ios":
            options = XCUITestOptions().load_capabilities(caps)
        else:
            raise Exception("Unknown platform:", platform)

        print(f"🚀 Creating driver on {url} ...")
        AppiumServerManager._driver = webdriver.Remote(url, options=options)

        return AppiumServerManager._driver

    @staticmethod
    def get_driver():
        return AppiumServerManager._driver
