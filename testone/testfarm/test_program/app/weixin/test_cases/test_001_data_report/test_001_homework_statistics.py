import unittest,time
import os
from testfarm.test_program.app.weixin.element.main_page import HomePage
from testfarm.test_program.app.weixin.element.master_page import MasterPage
from testfarm.test_program.app.weixin.element.index_page import IndexPage
from testfarm.test_program.app.weixin.element.homeword_statistics_page import HomeWorkStatistics
from testfarm.test_program.app.weixin.element.public import Get_Cash
from testfarm.test_program.app.weixin.test_cases.login_page import Loginpage
from testfarm.test_program.conf.decorator import testcase, setup, teardown
from testfarm.test_program.app.student.login.object_page.login_page import LoginPage
from testfarm.test_program.app.weixin.element.statement_page import Statement
PATH = lambda p: os.path.abspath(os.path.join(os.path.dirname(__file__), p))  # 获取当前路径

class Set_offer(unittest.TestCase):
    """作业统计"""

    @classmethod
    @setup
    def setUp(cls):
        """启动应用"""
        cls.index = IndexPage()
        cls.home = HomePage()
        cls.login_page = LoginPage()
        cls.master_page = MasterPage()
        cls.login = Loginpage()
        cls.statement_page = Statement()
        cls.homeworkstatistics = HomeWorkStatistics()
        cls.public = Get_Cash()
    @classmethod
    @teardown
    def tearDown(cls):
        pass

    @testcase
    def test_num_all(self):
        self.public.enter_wxzx()
        self.home.click_data_report()
        self.home.click_homework_statistics()
        if self.home.wait_homeword_statistics():
            # 上上周
            get_date = self.homeworkstatistics.get_date()
            expect_date = self.homeworkstatistics.last_weak(weeks=-2)
            self.judge_date(get_date,expect_date)
            # 上周
            self.homeworkstatistics.click_last_weak()
            get_date = self.homeworkstatistics.get_date()
            expect_date = self.homeworkstatistics.last_weak()
            self.judge_date(get_date,expect_date)
            # 上月
            self.homeworkstatistics.click_last_month()
            get_date = self.homeworkstatistics.get_date()
            expect_date = self.homeworkstatistics.last_month()
            self.judge_date(get_date,expect_date)
            # 点击学校
            self.homeworkstatistics.click_school()
            self.homeworkstatistics.click_school_ensure()
        if self.home.wait_homeword_statistics():
            # 点击教师
            self.homeworkstatistics.click_tea()
            self.homeworkstatistics.select_all()
            self.homeworkstatistics.click_reset()
            self.homeworkstatistics.click_first_tea()
            self.homeworkstatistics.click_ensure()
            self.homeworkstatistics.get_show_tea()
            self.homeworkstatistics.click_tea()
            self.homeworkstatistics.select_all()
            self.homeworkstatistics.click_ensure()
            # 点击 导出
            self.homeworkstatistics.click_export()
            self.homeworkstatistics.get_export_tips()
            self.homeworkstatistics.click_cancel()
            # 点击 对比
            self.homeworkstatistics.click_compared()
            ele_list = self.homeworkstatistics.get_all_info()
            ele_list[1].click()
            ele_list[3].click()
            self.homeworkstatistics.click_compared()
            self.homeworkstatistics.click_all()
            print('✅对比按钮（对比/全部）切换正常')
            # 点击 问号
            self.homeworkstatistics.click_help()
            if self.homeworkstatistics.wait_help_page():
                print('✅帮助界面跳转成功')
            else:
                print('\n\t❌error:帮助界面跳转失败，请进行检查\n')

            self.master_page.go_back()
            self.master_page.get_btn()  # 点击返回
            self.master_page.go_back()  # 点击返回
            if self.login_page.wait_check_page_index():
                self.login_page.click_weixin()
        print("脚本执行结束")

    def judge_date(self,get_date,expect_date):
        if get_date[0] == expect_date[0] and get_date[1] == expect_date[1]:
            print('✅日期显示正确')
        else:
            print('\n\t❌error:日期显示错误，实际显示时间为:%s,预期时间为:%s\n'%(get_date,expect_date))




