import unittest
from testfarm.test_program.app.weixin.element.main_page import HomePage
from testfarm.test_program.app.weixin.element.master_page import MasterPage
from testfarm.test_program.app.weixin.element.public import Get_Cash
from testfarm.test_program.app.weixin.test_cases.login_page import Loginpage
from testfarm.test_program.conf.decorator import testcase, setup, teardown
from testfarm.test_program.app.student.login.object_page.login_page import LoginPage
from testfarm.test_program.app.weixin.element.statement_page import Statement

class Set_offer(unittest.TestCase):
    """错误班级缴费查询"""

    @classmethod
    @setup
    def setUp(cls):
        """启动应用"""
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
    def test_class_bill_error(self):
        self.public.enter_wxzx()
        self.home.account_management()# 点击进入账户管理
        self.home.click_my_school() # 点击进入我的学校
        if self.statement_page.wait_check_page():
            self.statement_page.click_statement() #进入对账单
            self.statement_page.show_more_data() # 显示更多余额
            self.statement_page.click_class_money() # 点击班级交费
            if self.statement_page.judge_class_money(): # 判断班级交费
                self.statement_page.select_class_error() # 查询班级
                self.statement_page.ensure_seach().click() # 搜索
                self.master_page.go_back_down()  # 点击返回
                self.master_page.go_back_down()  # 点击返回
            else:
                print('❌error:进入页面错误')
        else:
            print('❌error:进入页面错误')
        print("脚本执行结束")

    def quit(self):
        self.master_page.go_back()  # 点击返回
        self.master_page.get_btn()  # 点击返回
        self.master_page.go_back()
        if self.login_page.wait_check_page_index():
            self.login_page.click_weixin()