import unittest
from testfarm.test_program.app.weixin.element.main_page import HomePage
from testfarm.test_program.app.weixin.element.master_page import MasterPage
from testfarm.test_program.conf.decorator import testcase, setup, teardown
from testfarm.test_program.app.student.login.object_page.login_page import LoginPage
from testfarm.test_program.app.weixin.element.statement_page import Statement
from testfarm.test_program.app.weixin.element.school_proxy_buy_page import SchoolProxyPage
from testfarm.test_program.app.weixin.element.public import Get_Cash


class Set_offer(unittest.TestCase):
    """代买"""
    @classmethod
    @setup
    def setUp(cls):
        """启动应用"""
        cls.home = HomePage()
        cls.login_page = LoginPage()
        cls.master_page = MasterPage()
        cls.statement_page = Statement()
        cls.school_proxy = SchoolProxyPage()
        cls.public = Get_Cash()

    @classmethod
    @teardown
    def tearDown(cls):
        pass
    @testcase
    def test_student_bill_error(self):
        self.public.enter_wxzx()
        self.home.account_management()# 点击进入账户管理
        self.home.click_my_school() # 点击进入我的学校
        before_info = self.public.test_num_all()
        if self.statement_page.wait_check_page():
            self.school_proxy.click_proxy_buy()
            if self.school_proxy.wait_buy_page():
                self.school_proxy.get_class_list()
                self.school_proxy.click_tea_li_class()
                if self.school_proxy.wait_choose_stu_page():
                    stu_ele = self.school_proxy.get_stu()
                    self.school_proxy.click_all()
                    self.school_proxy.click_all()
                    num = self.school_proxy.get_all_number()
                    self.judge_num(stu_ele,num)
                    self.school_proxy.click_next()
                    if self.school_proxy.wait_choose_card_page():
                        card_ele = self.school_proxy.get_all_card()
                        peo_num,unit_price = self.judge_cash(card_ele,num)
                        card_ele[0].click()
                        self.school_proxy.click_proxy_buy()
                        self.school_proxy.input_pwd()
                        self.school_proxy.click_ensure()
                        self.school_proxy.get_stu_info()
                        self.school_proxy.click_back()
                        self.school_proxy.click_back()
                        after_info = self.public.test_num_all()

                        self.public.school_info(before_info= before_info,after_info= after_info,peo_num= peo_num,unit_price= unit_price)
                        self.public.quit()
                    else:
                        print('❌error：进入页面错误')
                else:
                    print('❌error：进入页面错误')
            else:
                print('❌error：进入页面错误')
        else:
            print('❌error：进入页面错误')
        print('=====脚本执行完毕=====')

    def judge_num(self,ele,num):
        if len(ele) == num:
            print('✅学生数量正确')
        else:
            print('❌error:学生共计错误，ele:%s,get:%s'%(len(ele),num))

    def judge_cash(self,card_ele,num):
        price_list = [15,41,79,150]
        for i,j in enumerate(card_ele):
            if i < 4:
                j.click()
                cal = '%.2f'%(num * price_list[i])
            # elif i == 4:
            #     card_ele[-3].click()
            #     self.school_proxy.input_month()
            #     cal = '%.2f' % (num * price_list[0])
            # elif i == 5:
            #     card_ele[-2].click()
            #     self.school_proxy.input_daya()
            #     cal = '%.2f' % (num * price_list[0])
            elif i > 3:
                break
            cash = self.school_proxy.get_cash()
            if cash == cal:
                print('✅总金额正确')
            else:
                print('❌error:总金额有问题，请进行检查，cash:%s,计算得：%s' % (cash, cal))
        return num, price_list[0]