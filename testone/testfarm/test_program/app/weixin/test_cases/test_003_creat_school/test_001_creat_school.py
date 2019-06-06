#!/usr/bin/env python
# code:UTF-8
# @Author  : Sasuke
import unittest
from testfarm.test_program.app.weixin.element.main_page import HomePage
from testfarm.test_program.app.weixin.element.master_page import MasterPage
from testfarm.test_program.app.weixin.element.statement_page import Statement
from testfarm.test_program.conf.decorator import testcase, setup, teardown
from testfarm.test_program.app.student.login.object_page.login_page import LoginPage
from testfarm.test_program.app.weixin.element.creat_school_page import CreatSchoolPage
from testfarm.test_program.app.weixin.element.public import Get_Cash
from testfarm.test_program.app.weixin.element.opr_web import OprWeb

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
        cls.creat_school = CreatSchoolPage()
        cls.public = Get_Cash()
        cls.manager = OprWeb()

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
            self.creat_school.slip_up() # 滑动屏幕
            self.creat_school.click_creat_school() # 点击 创建学校
            if self.creat_school.wait_creat_school_page():
                self.creat_school.judge_tips_in_submit() # 判断页面提示信息
                self.creat_school.input_school_name('xxh高级中学') # 输入学校名称
                self.creat_school.input_nickname('xxh') # 输入学校简称
                self.creat_school.click_the_arrow() # 点击下拉箭头
                self.creat_school.choose_lacation() # 选择地点
                self.creat_school.click_ensure() # 点击确定
                self.creat_school.click_application() # 点击申请
                if self.creat_school.wait_creat_school_page():
                    self.creat_school.judge_tips_in_result()
                    self.creat_school.click_modify() # 点击 信息有误 重新填写
                    if self.creat_school.wait_creat_school_page():
                        self.creat_school.input_school_name('x-x-h高级中学')
                        self.creat_school.input_nickname('x-x-h')
                        self.creat_school.click_application()
                        if self.creat_school.wait_creat_school_page():
                            self.creat_school.judge_tips_in_result(name='x-x-h高级中学',nickname='x-x-h')
                            self.creat_school.click_back()
                            if self.creat_school.wait_school_page():
                                self.creat_school.get_new_school()
                                self.master_page.go_back()
                                self.master_page.get_btn()
                                self.master_page.go_back()
                                if self.login_page.wait_check_page_index():
                                    self.login_page.click_weixin()
                                    self.manager.refuse_application()
                                else:
                                    print('❌error:进入页面失败')
                            else:
                                print('❌error:进入页面失败')
                        else:
                            print('❌error:进入页面失败')
                    else:
                        print('❌error:进入页面失败')
                else:
                    print('❌error:进入页面失败')
            else:
                print('❌error:进入页面失败')
        else:
            print('❌error:进入页面失败')