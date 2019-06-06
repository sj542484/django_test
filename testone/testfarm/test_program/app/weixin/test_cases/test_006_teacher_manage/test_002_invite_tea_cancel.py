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
    """教师管理 取消教师申请"""
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
            self.change_name() # 修改名字
            self.canael_invite() # 取消邀请
            self.canael_invite() # 取消邀请
        else:
            print('\n\t❌error:进入页面错误，没有进入\n')
        self.master_page.go_back()  # 点击返回回到公众号主页面
        self.master_page.get_btn()  # 点击返回
        self.master_page.go_back()  # 点击返回
        if self.login_page.wait_check_page_index():
            self.login_page.click_weixin()

    def change_name(self):
        tea_ele_list = self.tea_manage.get_all_teacher()[1]
        tea_ele_list[-1].click()  # 点击邀请中的老师
        if self.tea_manage.wait_teacher_info_page():
            self.tea_manage.change_name_in_tea_info()
            self.tea_manage.save_change()
            if self.tea_manage.wait_teacher_manage_page():
                info_list = self.tea_manage.get_all_teacher()[0]
                if '时晓 邀请中 -' in str(info_list) and '小时 邀请中 -' in str(info_list):
                    print('✅姓名修改成功')
                else:
                    print('\n\t❌error:姓名修改失败，请进行检查\n')
            else:
                print('\n\t❌error:进入页面错误，没有进入\n')
        else:
            print('\n\t❌error:进入页面错误，没有进入\n')


    def canael_invite(self):
        all_tea_ele_list = self.tea_manage.get_all_teacher()[1]
        all_tea_ele_list[-1].click()
        if self.tea_manage.wait_teacher_info_page():
            tea_name = self.tea_manage.get_tea_name()
            self.tea_manage.invite_cancel()
            self.tea_manage.click_cancel()
            self.tea_manage.invite_cancel()
            self.tea_manage.click_ensure()
            info_list = self.tea_manage.get_all_teacher()[0]
            if '%s 邀请中 -'%tea_name not in str(info_list):
                print('✅取消邀请成功')
            else:
                print('\n\t❌error:取消邀请失败，请进行检查\n')
        else:
            print('\n\t❌error:进入页面错误，没有进入\n')