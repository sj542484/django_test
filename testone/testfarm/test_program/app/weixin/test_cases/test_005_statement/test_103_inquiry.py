import unittest
from testfarm.test_program.app.weixin.element.main_page import HomePage
from testfarm.test_program.app.weixin.element.master_page import MasterPage
from testfarm.test_program.app.weixin.element.public import Get_Cash
from testfarm.test_program.app.weixin.test_cases.login_page import Loginpage
from testfarm.test_program.conf.decorator import testcase, setup, teardown
from testfarm.test_program.app.student.login.object_page.login_page import LoginPage
from testfarm.test_program.app.weixin.element.statement_page import Statement
from testfarm.test_program.app.weixin.test_data.phone_list import student_number

class Set_offer(unittest.TestCase):
    """学生缴费查询"""
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
        self.public.enter_wxzx() # 进入万星
        self.home.account_management()# 点击进入账户管理
        self.home.click_my_school() # 点击进入我的学校
        if self.statement_page.wait_check_page():
            self.statement_page.click_statement() #进入对账单
            self.statement_page.click_doubt() # 点击 ？
            info_list,ele_list = self.statement_page.get_info() # 获取弹框信息
            self.judge_info(info_list) # 对信息进行判断
            ele_list[-1].click() # 关闭弹窗
            self.statement_page.show_more_data() # 显示更多余额
            self.statement_page.click_student_select() # 点击学生交费查询
            if self.statement_page.judge_select(): # 判断是否进入学生交费查询
                input_ele = self.statement_page.get_input()
                ensure_ele = self.statement_page.ensure_seach()
                stu_phone = self.public.search_verification(input_ele=(input_ele,),data=student_number,ensure_ele=ensure_ele)
                self.statement_page.show_student(stu_phone) # 显示学生信息
                self.statement_page.check_student_deail()
                self.quit()
            else:
                print('❌error:进入页面失败')
        else:
            print('❌error:进入页面失败')
        print("脚本执行结束")

    def quit(self):
        self.master_page.go_back()  # 点击返回
        self.master_page.get_btn()  # 点击返回
        self.master_page.go_back()  # 点击返回
        if self.login_page.wait_check_page_index():
            self.login_page.click_weixin()

    def judge_info(self,info_list):
        if info_list[0] == '提示':
            if info_list[1] == '1.数据为当前实时数据;':
                if info_list[2] == '2."提分版"人数: 使用"提分版"的人数;':
                    if info_list[3] == '3.试用人数:未交费但仍在"试用期"的人数;':
                        if info_list[4] == '×':
                            print('✅提示信息正确')
                        else:
                            print('❌error:提示信息异常，请进行检查')
                    else:
                        print('❌error:提示信息异常，请进行检查')
                else:
                    print('❌error:提示信息异常，请进行检查')
            else:
                print('❌error:提示信息异常，请进行检查')
        else:
            print('❌error:提示信息异常，请进行检查')