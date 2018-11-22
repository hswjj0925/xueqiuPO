# ! coding=utf-8

from .base import BasePage
import logging
from setting import initialization as initia

class HeaderPage(BasePage):
    def __init__(self):
        logging.info('init the header page')
        BasePage.__init__(self,initia.AppiumDriver.appium_driver)

    def locate_user_profile_icon(self):
        logging.info("寻找小牛icon")
        return self.ex_find_element('id','user_profile_container')

    def tap_user_profile_icon(self):
        logging.info("点击小牛icon")
        self.tap(self.locate_user_profile_icon())

    def locate_message_icon(self):
        logging.info("寻找信封icon")
        return self.ex_find_element('id','action_message')

    def tap_message_icon(self):
        logging.info("点击信封icon")
        self.tap(self.locate_message_icon())