from setting import initialization as initia
import logging
import pytest
import subprocess


initia.AppiumDriver.init_appium_driver()

fileHandler = logging.FileHandler(filename='../log/uiauto.log',encoding="utf-8")
logging.getLogger().setLevel(0)
formatter = logging.Formatter('%(asctime)s %(name)s %(levelname)s %(module)s:%(lineno)d %(message)s')
fileHandler.setFormatter(formatter)

logging.getLogger("urllib3.connectionpool").setLevel(logging.WARNING)
logging.getLogger("selenium.webdriver.remote.remote_connection").setLevel(logging.WARNING)

logging.getLogger().addHandler(fileHandler)

if __name__ == '__main__':
    print("start to execute test case")
    pytest.main(['-sq', '--alluredir', '../log/testreport', 'case/userlogin/test_login.py'])
    print(subprocess.getstatusoutput('/usr/local/bin/allure generate --clean ../log/testreport/ -o ../log/testreport/html'))