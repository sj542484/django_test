import unittest
from testfarm.test_program.app.weixin.element.main_page import HomePage
from testfarm.test_program.app.weixin.element.master_page import MasterPage
from testfarm.test_program.app.weixin.element.year_page import Year_page
from testfarm.test_program.app.weixin.element.statement_page import Statement
from testfarm.test_program.conf.decorator import testcase, setup, teardown
from testfarm.test_program.app.weixin.element.public import Get_Cash
from testfarm.test_program.app.weixin.element.offer_single_page import Offer_single

class Set_offer(unittest.TestCase):
    """取消年卡优惠价-查看分享"""
    @classmethod
    @setup
    def setUp(cls):
        """启动应用"""
        cls.home = HomePage()
        cls.master_page = MasterPage()
        cls.year_page = Year_page()
        cls.statement_page = Statement()
        cls.public = Get_Cash()
        cls.offer = Offer_single()

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
                self.year_page.click_year_cancel()  # 点击取消
                if self.year_page.click_cancel_wait():
                    self.year_page.click_cancel() # 点击取消
                    self.year_page.send_pwd() # 发送密码
                    self.year_page.click_determine() # 点击确定
                    if self.master_page.wait_set_page():
                        self.year_page.cancel_success_judge()
                        self.public.quit()
                        self.public.enter_friend()
                        info_list = self.offer.get_card_info()
                        self.judge_info(info_list)
                        self.master_page.go_back()
                    else:
                        print('❌error:进入页面错误')
                else:
                    print('❌error:进入页面错误')
            else:
                print('❌error:进入页面错误')
        else:
            print('❌error:进入页面错误')
        print('=====脚本执行完毕=====')


    def judge_info(self,info_list):
        if len(info_list) == 1 and info_list[0][0] == '半年卡':
            print('✅年卡取消成功')
        else:
            print('❌error:年卡取消失败，请进行检查，crad_info:%s'%info_list)