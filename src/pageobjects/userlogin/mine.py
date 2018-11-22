#coding=utf-8

import logging

from pageobjects.base import BasePage
from setting import initialization as initia

class MinePage(BasePage):
    def __init__(self):
        logging.info('init mine page')
        BasePage.__init__(self,initia.AppiumDriver.appium_driver)

    def locate_login_button(self):
        logging.info('查找登陆雪球按钮')
        return self.ex_find_element('id',"tv_login")

    def tap_login_button(self):
        logging.info('点击登陆雪球按钮')
        self.tap(self.locate_login_button())

    def locate_login_with_phone_other(self):
        logging.info('查找手机及其他按钮')
        return self.ex_find_element('id','tv_login_by_phone_or_others')

    def tap_login_with_phone_other(self):
        logging.info('点击登陆手机及其他按钮')
        self.tap(self.locate_login_with_phone_other())

    def locate_login_with_account(self):
        logging.info('查找邮箱手机号密码按钮')
        return self.ex_find_element('id','tv_login_with_account')

    def tap_login_with_account(self):
        logging.info('点击邮箱手机号密码按钮')
        self.tap(self.locate_login_with_account())

