#coding=utf-8

import pytest
import allure

from pageobjects.header import HeaderPage
from pageobjects.userlogin.login import LoginPage
from pageobjects.userlogin.mine import MinePage
import pytest


@allure.feature('测试登陆功能')
class TestLogin:

    #我的->登陆雪球->手机及其他登录->邮箱手机号密码登录—>输入账号密码->点击登陆
    @allure.story('测试登陆功能')
    def test_0001(self):
        with allure.step('点击小动物Icon,切换到登陆页面'):
            header_page = HeaderPage()
            header_page.tap_user_profile_icon()

        with allure.step('点击登陆雪球'):
            mine_page = MinePage()
            mine_page.tap_login_button()

        with allure.step('点击手机及其他登录'):
            mine_page.tap_login_with_phone_other()

        with allure.step('点击手机号密码登录'):
            mine_page.tap_login_with_account()

        with allure.step('登陆雪球'):
            login_page = LoginPage()
            login_page.login_with_phone_and_password('18610648684','...wjj900925')

