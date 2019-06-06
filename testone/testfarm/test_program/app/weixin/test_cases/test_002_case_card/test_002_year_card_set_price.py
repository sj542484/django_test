import unittest
from testfarm.test_program.app.weixin.element.main_page import HomePage
from testfarm.test_program.app.weixin.element.master_page import MasterPage
from testfarm.test_program.app.weixin.element.year_page import Year_page
import time
from testfarm.test_program.app.weixin.element.public import Get_Cash
from testfarm.test_program.app.weixin.element.statement_page import Statement
from testfarm.test_program.app.weixin.test_data.set_price import priceList
from testfarm.test_program.conf.decorator import testcase, setup, teardown
from testfarm.test_program.app.student.login.object_page.login_page import LoginPage

class Set_offer(unittest.TestCase):
    """设置年卡优惠价-购买"""
    @classmethod
    @setup
    def setUp(cls):
        """启动应用"""
        cls.home = HomePage()
        cls.login_page = LoginPage()
        cls.master_page = MasterPage()
        cls.year_page = Year_page()
        cls.statement_page = Statement()
        cls.public = Get_Cash()

    @classmethod
    @teardown
    def tearDown(cls):
        pass

    @testcase
    def test_offer(self):
        self.public.enter_wxzx()
        self.home.account_management()# 点击进入账户管理
        self.home.click_my_school() # 点击进入我的学校
        if self.statement_page.wait_check_page():
            self.master_page.set_price()  # 设置优惠价进入设置优惠条目
            if self.master_page.wait_set_page():
                self.master_page.click_set_year()
                self.master_page.set_password()
                self.master_page.click_determine()
                self.set_price()
                self.share_card()
                self.public.quit()
                self.public.single_pay(card_price=priceList[-1][1], card_type='年卡')
        else:
            print('❌error:进入页面失败，请进行检查')
        print('=====脚本执行完毕=====')


    def set_price(self):
        '''设置价格'''
        for price in priceList:
            expectStatue = self.year_page.expect_statue(price)
            if self.year_page.set_price_wait():
                self.year_page.set_price(price)
                # 输入完成点击确定
                self.year_page.click_ensure()
                # 进行状态判断
                judgeStatue = self.year_page.judge_statue()
                if expectStatue == judgeStatue:
                    print('✅价格设置模块正常')
                else:
                    print('❌error:设置价格异常,price:%s,active:%s' % (price, judgeStatue))
                time.sleep(2)
            else:
                print('❌error:进入页面失败，请进行检查')

    def share_card(self):
        self.master_page.share_card() # 点击 分享优惠页
        self.master_page.click_more() # 点击 更多
        self.master_page.click_share_friend()
        self.master_page.click_myself()
        self.master_page.click_send()