# ! coding=utf-8

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By
import time
import logging

class BasePage:
    def __init__(self, appium_driver):
        self.appium_driver = appium_driver

    def ex_find_element(self,type,value):
        '''
        :param type:id,xpath,class_name
        :param value:id_value,xpath
        :return:found element or false
        '''

        retry_time = 3
        sleep_time = 1
        found_element = ''

        while retry_time:
            try:
                if type.strip() == 'xpath':
                    found_element = self.appium_driver.find_element_by_xpath(value)
                elif type.strip() == 'id':
                    found_element = self.appium_driver.find_element_by_id(value)
                elif type.strip() == 'class_name':
                    found_element = self.appium_driver.find_element_by_class_name(value)
                elif type.strip() == 'css_selector':
                    pass
                else:
                    logging.warning("the input is wrong")
                return found_element
            except:
                logging.warning('Can not find element,will retry at'+str(4-retry_time)+'time')
                time.sleep(sleep_time+4-retry_time)
                retry_time=retry_time-1
        return False


    def tap(self,element):
        element.click()


    def set_value(self,element,value):
        '''

        :param element:
        :param value:
        :return:
        '''

        element.clear()
        element.click()
        logging.info("setting value to "+str(value))
        element.send_keys(value)

    def get_text_by_element(self,element):
        return element.text
