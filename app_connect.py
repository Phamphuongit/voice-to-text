from appium.options.android import UiAutomator2Options
from appium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from test_variables import *

class App_Connect():
    def __init__(self):
        self.options = UiAutomator2Options()
        self.options.platform_name = APP_CONFIG["platform_name"]
        self.options.automation_name = APP_CONFIG["automation_name"]
        self.options.device_name = APP_CONFIG["device_name"]
        self.options.app_package = APP_CONFIG["app_package"]
        self.options.app_activity = APP_CONFIG["app_activity"]
        self.options.language = "en"
        self.options.locale = "US"
        self.options.no_reset = True

        self.appium_server_url = "http://localhost:4723"

    def open_app(self):
        self.driver = webdriver.Remote(self.appium_server_url, options=self.options)

    def wait(self):
        return WebDriverWait(self.driver, 15)
    
    def teardown(self):
        if self.driver:
            self.driver.quit()
            
    def terminate_app(self):
        self.driver.terminate_app("com.vingroup.VinIDMerchantApp")
