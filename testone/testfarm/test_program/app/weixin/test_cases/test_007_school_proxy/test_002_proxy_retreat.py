import unittest,time
from testfarm.test_program.app.weixin.element.main_page import HomePage
from testfarm.test_program.app.weixin.element.master_page import MasterPage
from testfarm.test_program.conf.decorator import testcase, setup, teardown
from testfarm.test_program.app.student.login.object_page.login_page import LoginPage
from testfarm.test_program.app.weixin.element.statement_page import Statement
from testfarm.test_program.app.weixin.element.school_proxy_sale_page import SchoolProxySalePage
from testfarm.test_program.app.weixin.test_data.phone_list import pwd_retreat,PhoneList
from testfarm.test_program.app.weixin.element.public import Get_Cash


class Set_offer(unittest.TestCase):
    """代退"""
    @classmethod
    @setup
    def setUp(cls):
        """启动应用"""
        cls.home = HomePage()
        cls.login_page = LoginPage()
        cls.master_page = MasterPage()
        cls.statement_page = Statement()
        cls.school_proxy = SchoolProxySalePage()
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
            self.school_proxy.click_proxy_sale()
            if self.school_proxy.wait_sale_page():
                self.school_proxy.get_page_info()
                self.school_proxy.judge_phone()
                self.school_proxy.input_stu_phone(PhoneList[-1])
                self.school_proxy.click_search()
                info_before = self.school_proxy.get_stu_info()
                order_num_before = self.school_proxy.get_order()
                get_num_before = self.school_proxy.get_num_in_page()
                no_num_before = self.school_proxy.no_num()
                self.judge_num(get_num_before,order_num_before,no_num_before)

                self.school_proxy.click_second_order()
                self.school_proxy.get_order_info()
                self.school_proxy.get_refundable_amount()
                self.school_proxy.click_refund()
                self.school_proxy.click_cancel()

                self.school_proxy.click_first_order()
                self.school_proxy.get_order_info()
                self.school_proxy.click_refund()
                self.school_proxy.input_pwd().send_keys('123321')
                self.judge_pwd_hide('••••••')
                self.school_proxy.click_hide()
                self.judge_pwd_hide('123321')
                self.school_proxy.click_ensure()
                if self.school_proxy.wait_refund_success_page():
                    self.school_proxy.click_back()
                    if self.statement_page.wait_check_page():
                        self.school_proxy.click_proxy_sale()
                        if self.school_proxy.wait_sale_page():
                            self.school_proxy.input_stu_phone(PhoneList[-1])
                            self.school_proxy.click_search()
                            info_after = self.school_proxy.get_stu_info()
                            self.judge_data(info_after,info_before)
                            order_num_after = self.school_proxy.get_order()
                            get_num_after = self.school_proxy.get_num_in_page()
                            no_num_after = self.school_proxy.no_num()
                            self.judge_num(get_num_after, order_num_after, no_num_after)
                            if get_num_before - get_num_after == 1:
                                print('✅订单数量递减成功')
                            else:
                                print('❌error:订单数量递减异常 请进行检查，get_num_before:%s,get_num_after:%s'%(get_num_before,get_num_after))
                            self.school_proxy.click_back()
                            after_info = self.public.test_num_all()
                            self.public.school_info(before_info= before_info,after_info= after_info,opr_type='代退')
                            self.public.quit()
                        else:
                            print('❌error：进入页面错误')
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


    def judge_pwd_hide(self,content):
        if self.school_proxy.input_pwd(text=content).text == content:
            print('✅显示密码功能正常')
        else:
            print('❌error:显示密码功能异常，请进行检查')

    def judge_data(self,info_after,info_before):
        if info_before[0] == info_after[0]:
            data_before = info_before[1][4:]
            data_after = info_after[1][4:]
            expect_data = self.school_proxy.expect_data(data_before)
            if data_after == expect_data:
                print('✅日期正常')
            else:
                print('❌error:日期异常，请进行检查')
        else:
            print('❌error:学生名称不一致，请进行检查')

    def judge_num(self,get_num,order_num,no_num):
        if get_num == order_num - no_num:
            print('✅可退订单数量显示正常')
        else:
            print('❌error:可退订单数量显示异常，请进行检查')