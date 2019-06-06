#!/usr/bin/env python
# code:UTF-8
# @Author  : Sasuke
import unittest,time
from testfarm.test_program.app.weixin.element.main_page import HomePage
from testfarm.test_program.app.weixin.element.master_page import MasterPage
from testfarm.test_program.app.weixin.element.statement_page import Statement
from testfarm.test_program.conf.decorator import testcase, setup, teardown
from testfarm.test_program.app.student.login.object_page.login_page import LoginPage
from testfarm.test_program.app.weixin.element.teacher_manage import TeacherManage
from testfarm.test_program.app.weixin.element.public import Get_Cash

class Set_offer(unittest.TestCase):
    """教师管理 添加教师"""
    @classmethod
    @setup
    def setUp(cls):
        """启动应用"""
        cls.home = HomePage()
        cls.login_page = LoginPage()
        cls.master_page = MasterPage()
        cls.statement_page = Statement()
        cls.tea_manage = TeacherManage()
        cls.public = Get_Cash()
    @classmethod
    @teardown
    def tearDown(cls):
        pass

    @testcase
    def test_offer(self):
        self.public.enter_wxzx()
        self.home.account_management()# 点击进入账户管理
        self.home.click_teacher_manage() # 点击进入教师管理
        if self.tea_manage.wait_teacher_manage_page():
            self.tea_manage.get_all_teacher()
            self.tea_manage.click_invite_tea()
            if self.tea_manage.wait_creat_tea_page():
                self.tea_manage.get_info()
                self.tea_manage.input_tea_info()
                self.tea_manage.click_preview()
                if self.tea_manage.wait_preview_page():
                    if self.tea_manage.check_tips():
                        self.tea_manage.completion_phone_top()
                        self.tea_manage.hide_key_board()
                        self.tea_manage.completion_phone_bottom()
                        self.tea_manage.hide_key_board()
                        self.tea_manage.change_name()
                        self.tea_manage.click_invite_ensure()
                        if self.tea_manage.wait_succeed_page():
                            self.tea_manage.succeed_info()
                            # self.tea_manage.click_here()
                            # if self.tea_manage.wait_jump_page():
                            #     print('✅页面跳转成功')
                            # else:
                            #     print('\n\t❌error:页面跳转失败，请进行检查\n')
                            self.tea_manage.click_back()
                            self.judge_invite()
                    else:
                        print('\n\t❌error:提示信息异常，请进行检查\n')
                else:
                    print('\n\t❌error:进入页面错误，没有进入\n')
            else:
                print('\n\t❌error:进入页面错误，没有进入\n')
        else:
            print('\n\t❌error:进入页面错误，没有进入\n')
        self.master_page.go_back()  # 点击返回回到公众号主页面
        self.master_page.get_btn()  # 点击返回
        self.master_page.go_back()  # 点击返回
        if self.login_page.wait_check_page_index():
            self.login_page.click_weixin()

    def judge_invite(self):
        info_list = self.tea_manage.get_all_teacher()[0]
        if '时晓 邀请中 -' in str(info_list) and 'xxh 邀请中 -' in str(info_list):
            print('✅申请成功')
        else:
            print('\n\t❌error:申请添加失败，请进行检查\n')