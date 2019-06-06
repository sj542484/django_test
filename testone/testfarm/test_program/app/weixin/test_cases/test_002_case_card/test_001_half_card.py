import unittest
from testfarm.test_program.app.weixin.element.main_page import HomePage
from testfarm.test_program.app.weixin.element.master_page import MasterPage
from testfarm.test_program.conf.decorator import testcase, setup, teardown
from testfarm.test_program.app.weixin.element.statement_page import Statement
from testfarm.test_program.app.weixin.element.public import Get_Cash

class Set_offer(unittest.TestCase):
    """设置半年卡优惠价-购买"""
    @classmethod
    @setup
    def setUp(cls):
        """启动应用"""
        cls.home = HomePage()
        cls.master_page = MasterPage()
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
                self.master_page.click_set_half()  # 点击设置按钮
                self.master_page.set_password() # 点击请输入密码
                self.master_page.click_determine()  # 点击确定
                price = self.master_page.set_normal_price() #点击输入的价格
                self.master_page.click_again_determine()  # 点击确定
                self.share_card()
                self.public.quit()
                self.public.single_pay(card_price=price,card_type='半年卡')
                self.public.enter_friend(statue='long_press')
            else:
                print('❌error:进入页面错误，请进行检查')
        else:
            print('❌error:进入页面错误，请进行检查')
        print('=====脚本执行完毕=====')


    def share_card(self):
        self.master_page.share_card() # 点击 分享优惠页
        self.master_page.click_more() # 点击 更多
        self.master_page.click_share_friend()
        self.master_page.click_myself()
        self.master_page.click_send()