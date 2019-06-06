#!/usr/bin/env python
# code:UTF-8
# @Author  : Sasuke
import unittest
from testfarm.test_program.app.weixin.element.main_page import HomePage
from testfarm.test_program.app.weixin.element.master_page import MasterPage
from testfarm.test_program.app.weixin.element.statement_page import Statement
from testfarm.test_program.conf.decorator import testcase, setup, teardown
from testfarm.test_program.app.student.login.object_page.login_page import LoginPage
from testfarm.test_program.app.weixin.element.school_library import Library
from testfarm.test_program.app.weixin.element.public import Get_Cash

class Set_offer(unittest.TestCase):
    """设置年卡优惠价"""
    @classmethod
    @setup
    def setUp(cls):
        """启动应用"""
        cls.home = HomePage()
        cls.login_page = LoginPage()
        cls.master_page = MasterPage()
        cls.statement_page = Statement()
        cls.library = Library()
        cls.public = Get_Cash()
    @classmethod
    @teardown
    def tearDown(cls):
        pass

    @testcase
    def test_offer(self):
        self.public.enter_wxzx()
        self.home.account_management()  # 点击进入账户管理
        self.home.click_my_school()  # 点击进入我的学校
        if self.statement_page.wait_check_page():
            self.library.click_library() # 点击 本校图书馆
            self.library.get_active_tea()
            self.library.click_wenhao()
            self.library.get_tips_info()
            self.library.click_known()
            self.library.click_modify()
            ele,info = self.library.get_all_tea_info()
            index = 0
            self.library.choose_tea(tea_ele=ele,index=index)
            self.library.choose_ok()
            act_info = self.library.get_active_tea()
            if act_info == info:
                print('✅修改成功')
            else:
                print('❌error:')
        else:
            print('❌error:进入页面失败')