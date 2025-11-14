# Edot Mobile Automation

Automated test framework for **Edot Mobile App** using **Python**, **Appium**, **Pytest**, and **Allure**.

This framework supports **Android** and **iOS** devices and automatically handles device permissions.

---

##  Table of Contents

      1. [Requirements](#requirements)  
      2. [Installation](#installation)  
      3. [Project Structure](#project-structure)  
      4. [Capabilities Configuration](#capabilities-configuration)  
      5. [Running Tests](#running-tests)
      6. [Generating Test Report](#generating-test-report)  


---

##  Requirements

    - Python 3.10+  
    - Appium 2.x  
    - Node.js 18+  
    - Android Studio / iOS Xcode for devices/emulators  
    - pip packages: `appium-python-client`, `pytest`, `allure-pytest`  

---

##  Installation

    1. Clone this repository:
    git clone https://github.com/kennyRamadhan/edot_mobile.git
    cd edot_mobile
    
    2. Create virtual environment:
    python -m venv venv
    source venv/bin/activate  # Mac/Linux
    venv\Scripts\activate     # Windows
    
    3. Install Python Dependencies
    
    pip install -r requirements.txt
    
    
    4. Install Appium (if not installed):
    
    npm install -g appium
    
    5. Install Android/iOS drivers:
    
    appium driver install uiautomator2
    appium driver install xcuitest


## Project Structure

    edot_mobile/
    │
    ├─ config/
    │   ├─ capabilities_android.json
    │   └─ capabilities_ios.json
    │
    ├─ core/
    │   ├─ appium_server_manager.py
    │   └─ DriverManager.py
    │
    ├─ tests/
    │   └─ login_test.py
    │
    ├─ requirements.txt
    └─ conftest.py

## Capabilities Configuration
    Android Example
    {
      "platformName": "Android",
      "automationName": "UiAutomator2",
      "deviceName": "Android Emulator",
      "udid": "8e7553f8",
      "appPackage": "id.edot.ework",
      "appActivity": "id.edot.onboarding.ui.splash.SplashScreenActivity",
      "noReset": false,
      "newCommandTimeout": 300,
      "autoGrantPermissions": true
    }
    
    
    iOS Example
    {
      "platformName": "iOS",
      "automationName": "XCUITest",
      "deviceName": "iPhone 14",
      "platformVersion": "17.0",
      "app": "/path/to/app.app",
      "autoAcceptAlerts": true
    }
## Running Test

    Run all tests:
    
    pytest -s
    
    Run specific test with device selection:
    
    pytest -k login --device android -s
    pytest -k login --device ios -s



## Generate Reports

    pytest --alluredir=allure-results
    allure serve allure-results


