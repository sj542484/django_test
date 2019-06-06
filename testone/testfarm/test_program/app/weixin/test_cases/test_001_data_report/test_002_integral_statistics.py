import unittest,time
from testfarm.test_program.app.weixin.element.main_page import HomePage
from testfarm.test_program.app.weixin.element.master_page import MasterPage
from testfarm.test_program.app.weixin.element.index_page import IndexPage
from testfarm.test_program.app.weixin.element.integral_statistics_page import Integral_Statistics
from testfarm.test_program.app.weixin.element.public import Get_Cash
from testfarm.test_program.app.weixin.test_cases.login_page import Loginpage
from testfarm.test_program.conf.decorator import testcase, setup, teardown
from testfarm.test_program.app.student.login.object_page.login_page import LoginPage
from testfarm.test_program.app.weixin.element.statement_page import Statement

class Set_offer(unittest.TestCase):
    """积分统计"""
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
        cls.integral_statistics = Integral_Statistics()
        cls.public = Get_Cash()

    @classmethod
    @teardown
    def tearDown(cls):
        pass

    @testcase
    def test_num_all(self):
        self.public.enter_wxzx()
        self.home.click_data_report()
        self.home.click_integral_statistics()
        if self.home.wait_integral_statistics():
            # 点击学校
            self.integral_statistics.click_school()
            self.integral_statistics.click_school_ensure()
            # 点击时间
            self.integral_statistics.click_time()
            self.integral_statistics.click_next_type()
            self.integral_statistics.click_cancel()
            self.integral_statistics.click_time()
            self.integral_statistics.click_ensure()
            info = self.integral_statistics.get_time()
            self.judge_time(info)
            # 点击类型
            self.integral_statistics.click_type()
            # self.integral_statistics.click_next_type()
            self.integral_statistics.click_cancel()
            self.integral_statistics.click_type()
            self.integral_statistics.click_ensure()
            type_info = self.integral_statistics.get_type()
            self.judge_type(type_info)
            # 点击 对比  ---> 暂无数据
            # self.homeworkstatistics.click_compared()
            # ele_list = self.homeworkstatistics.get_all_info()
            # ele_list[1].click()
            # ele_list[3].click()
            # self.homeworkstatistics.click_compared()
            # self.homeworkstatistics.click_all()
            # print('✅对比按钮（对比/全部）切换正常')
            # 点击 问号
            self.integral_statistics.click_help()
            if self.integral_statistics.wait_help_page():
                print('✅帮助界面跳转成功')
            else:
                print('\n\t❌error:帮助界面跳转失败，请进行检查\n')
            # 返回主界面
            self.master_page.go_back()
            self.master_page.get_btn()
            self.master_page.go_back()
            if self.login_page.wait_check_page_index():
                self.login_page.click_weixin()
        print("脚本执行结束")

    def judge_date(self,get_date,expect_date):
        if get_date[0] == expect_date[0] and get_date[1] == expect_date[1]:
            print('✅日期显示正确')
        else:
            print('\n\t❌error:日期显示错误，实际显示时间为:%s,预期时间为:%s\n'%(get_date,expect_date))

    def judge_time(self,info):
        if info == '上周':
            print('✅切换正常')
        else:
            print('\n\t❌error:时间段切换异常 请进行检查\n')

    def judge_type(self,info):
        if info == '星星数量':
            print('✅切换正常')
        else:
            print('\n\t❌error:类型切换错误，请进行检查\n')