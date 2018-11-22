#coding=utf-8
from appium import webdriver

class AppiumDriver:
    appium_driver = ''

    @staticmethod
    def init_appium_driver():
        caps = {}
        caps["deviceName"] = "192.168.56.101:5555"
        caps["platformName"] = "Android"
        caps["appPackage"] = "com.xueqiu.android"
        caps["appActivity"] = ".view.WelcomeActivityAlias"
        caps["unicodeKeyBoard"] = "true"
        caps["resetKeyBoard"] = "true"
        caps["automationName"] = "UiAutomator2"
        caps["noReset"] = "true"
        AppiumDriver.appium_driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
        AppiumDriver.appium_driver.implicitly_wait(10)
