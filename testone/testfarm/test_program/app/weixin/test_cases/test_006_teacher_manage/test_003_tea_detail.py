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
    """教师管理 转班"""
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
        self.change_classes() # 转班
        self.recovery() # 复原
        self.public.quit() # 回首页
        print('=====脚本执行完毕=====')

    def change_classes(self):
        if self.tea_manage.wait_teacher_manage_page():
            time.sleep(3)
            tea_ele_list = self.tea_manage.get_all_teacher()[1]
            tea_ele_list[1].click()  # 点击 第二个老师dada
            if self.tea_manage.wait_teacher_info_page():
                self.tea_manage.get_tea_info()
                ele_list = self.tea_manage.class_list()[0]
                ele_list[0].click()
                if self.tea_manage.wait_tea_class_page():
                    self.tea_manage.class_info()
                    self.tea_manage.stu_info()
                    self.tea_manage.click_change_classes()  # 点击 转班
                    if self.tea_manage.wait_change_classes_page():
                        self.tea_manage.show_class_info()
                        ele_list = self.tea_manage.all_tea_to_change()
                        for i in ele_list:
                            time.sleep(0.2)
                            i.click()
                        self.tea_manage.click_ensure_change()
                        self.tea_manage.input_pwd()
                        self.tea_manage.click_ensure_pwd()
                        if self.tea_manage.wait_teacher_info_page():
                            class_info = self.tea_manage.class_list()[1]
                            if '[9259]李老师班级 全班4人，"提分版"4人' not in str(class_info):
                                print('✅班级转出成功')
                            else:
                                print('\n\t❌error:班级转出失败，请进行检查\n')
                        self.tea_manage.click_back()
                    else:
                        print('\n\t❌error:进入页面错误，没有进入\n')
                else:
                    print('\n\t❌error:进入页面错误，没有进入\n')
            else:
                print('\n\t❌error:进入页面错误，没有进入\n')
        else:
            print('\n\t❌error:进入页面错误，没有进入\n')

    def recovery(self):
        if self.tea_manage.wait_teacher_manage_page():
            tea_ele_list = self.tea_manage.get_all_teacher()[1]
            tea_ele_list[2].click()  # 点击最后一个老师
            if self.tea_manage.wait_teacher_info_page():
                class_info = self.tea_manage.class_list()
                if '[9259]李老师班级 全班4人，"提分版"4人 ' in str(class_info[1]):
                    print('✅班级转入成功')
                    class_info[0][0].click()
                    if self.tea_manage.wait_tea_class_page():
                        self.tea_manage.click_change_classes()  # 点击 转班
                        if self.tea_manage.wait_change_classes_page():
                            ele_list = self.tea_manage.all_tea_to_change()
                            ele_list[1].click()  # 点击老师
                            self.tea_manage.click_ensure_change()
                            self.tea_manage.input_pwd()
                            self.tea_manage.click_ensure_pwd()
                            if self.tea_manage.wait_teacher_info_page():
                                time.sleep(3)
                                class_info = self.tea_manage.class_list()[1]
                                if '[9259]李老师班级 全班4人，"提分版"1人' not in str(class_info):
                                    print('✅班级转出成功')
                                else:
                                    print('\n\t❌error:班级转出失败，请进行检查\n')
                                self.tea_manage.click_back()
                                if self.tea_manage.wait_teacher_manage_page():
                                    tea_ele_list = self.tea_manage.get_all_teacher()[1]
                                    tea_ele_list[1].click()  # 点击第二个老师
                                    if self.tea_manage.wait_teacher_info_page():
                                        time.sleep(3)
                                        class_info = self.tea_manage.class_list()
                                        if '[9259]李老师班级 全班4人，"提分版"1人' in str(class_info[1]):
                                            print('✅班级转入成功')
                                        else:
                                            print('\n\t❌error:班级转入失败，请进行检查\n')
                                    else:
                                        print('\n\t❌error:进入页面错误，没有进入\n')
                                else:
                                    print('\n\t❌error:进入页面错误，没有进入\n')
                            else:
                                print('\n\t❌error:进入页面错误，没有进入\n')
                        else:
                            print('\n\t❌error:进入页面错误，没有进入\n')
                    else:
                        print('\n\t❌error:进入页面错误，没有进入\n')
                else:
                    print('❌error:班级转入失败，请进行检查')
            else:
                print('\n\t❌error:进入页面错误，没有进入\n')
        else:
            print('\n\t❌error:进入页面错误，没有进入\n')