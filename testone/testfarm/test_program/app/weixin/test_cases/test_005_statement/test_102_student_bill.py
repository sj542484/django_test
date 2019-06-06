import unittest
from testfarm.test_program.app.weixin.element.main_page import HomePage
from testfarm.test_program.app.weixin.element.master_page import MasterPage
from testfarm.test_program.app.weixin.element.public import Get_Cash
from testfarm.test_program.app.weixin.test_cases.login_page import Loginpage
from testfarm.test_program.conf.decorator import testcase, setup, teardown, teststep
from testfarm.test_program.app.student.login.object_page.login_page import LoginPage
from testfarm.test_program.app.weixin.element.statement_page import Statement

class Set_offer(unittest.TestCase):
    """查看校长账单"""

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
    def test_student_bill(self):
        self.public.enter_wxzx()
        self.home.account_management()# 点击进入账户管理
        self.home.click_my_school() # 点击进入我的学校

        if self.statement_page.wait_check_page():
            self.statement_page.click_statement() #进入对账单

            self.statement_page.show_more_data() # 显示更多余额
            self.statement_page.click_enter_bill()# 点击进入学校账单
            if self.statement_page.judge_enter_bill(): # 判断是否进入账单
                data = self.statement_page.get_all_order()
                self.judge_data(data)
                self.statement_page.change_time() # 点击修改时间
                self.statement_page.click_determine() # 点击确定

                # 推出返回微信主界面
                self.master_page.go_back_down()  # 点击<返回
                self.master_page.go_back_down()  # 点击<返回
                self.master_page.go_back()  # 点击X返回
                self.master_page.get_btn() # < 返回公众号列表
                self.master_page.go_back() # < 退出公众号列表
                if self.login_page.wait_check_page_index():
                    self.login_page.click_weixin()

        print("脚本执行结束")

    def judge_data(self,data):
        sta = 0
        for j, i in enumerate(data):
            print(i)
            if len(i) != 4 and i[0] != '付款':
                print('❌订单数据异常，请检查', i)
                sta += 1
            if i[0] not in str('操作动作：收款、付款、月结、代买、代退'):
                print('❌操作动作异常，', i[0])
                sta += 1
            if j > 0:
                if int(i[2].split('-')[1]) > int(data[j - 1][2].split('-')[1]):
                    print('❌：排序错误，日期；', i, ';', data[j - 1])
                    sta += 1
        if sta == 0:
            print('✅订单数据正常，排序正常')