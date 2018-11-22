from pageobjects.base import BasePage
import logging
from setting import initialization as initia
from .mine import MinePage
from pageobjects.header import HeaderPage


class LoginPage(BasePage):
    def __init__(self):
        logging.info('init loggin page')
        BasePage.__init__(self,initia.AppiumDriver.appium_driver)

    def locate_login_account(self):
        logging.info('查找输入手机号框')
        return self.ex_find_element('id','login_account')

    def set_login_account_value(self,value):
        logging.info('点击输入手机号框,输入值')
        self.set_value(self.locate_login_account(),"18610648684")

    def locate_login_password(self):
        logging.info('查找输入密码框')
        return self.ex_find_element('id','login_password')

    def set_login_password_value(self,value):
        logging.info('点击输入密码框,输入值')
        self.set_value(self.locate_login_password(),"...wjj900925")

    def locate_login_button(self):
        logging.info('查找登陆按钮')
        return self.ex_find_element('id', 'button_next')

    def tap_login_button(self):
        logging.info('点击登陆按钮')
        self.tap(self.locate_login_button())

    #登陆方法
    def login_with_phone_and_password(self,phone_number,password):
        self.locate_login_account()
        self.set_login_account_value(phone_number)
        self.locate_login_password()
        self.set_login_password_value(password)
        self.tap_login_button()



