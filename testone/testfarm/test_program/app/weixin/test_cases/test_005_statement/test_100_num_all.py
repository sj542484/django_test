import unittest
from testfarm.test_program.app.weixin.element.main_page import HomePage
from testfarm.test_program.app.weixin.element.master_page import MasterPage
from testfarm.test_program.app.weixin.element.index_page import IndexPage
from testfarm.test_program.app.weixin.element.public import Get_Cash
from testfarm.test_program.app.weixin.test_cases.login_page import Loginpage
from testfarm.test_program.conf.decorator import testcase, setup, teardown
from testfarm.test_program.app.student.login.object_page.login_page import LoginPage
from testfarm.test_program.app.weixin.element.statement_page import Statement

class Set_offer(unittest.TestCase):
    """对账单页面的信息"""

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
        cls.public = Get_Cash()

    @classmethod
    @teardown
    def tearDown(cls):
        pass

    @testcase
    def test_num_all(self):
        self.public.enter_wxzx()
        self.home.account_management()# 点击进入账户管理
        self.home.click_my_school() # 点击进入我的学校
        if self.statement_page.wait_check_page():
            self.statement_page.click_statement() #进入对账单
            if self.statement_page.show_statement_num_wait():
                self.statement_page.show_statement_num() # 进入对账单页面
                self.statement_page.show_month_price() # 显示本月总额
                self.statement_page.show_school_money() # 学校余额是多少
                self.master_page.go_back()  # 点击返回
                self.master_page.get_btn()  # 点击返回
                self.master_page.go_back()  # 点击返回
                if self.login_page.wait_check_page_index():
                    self.login_page.click_weixin()
                print("脚本执行结束")