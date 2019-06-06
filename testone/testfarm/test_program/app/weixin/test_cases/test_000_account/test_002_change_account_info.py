import unittest,time
from testfarm.test_program.app.weixin.element.main_page import HomePage
from testfarm.test_program.app.weixin.element.master_page import MasterPage
from testfarm.test_program.app.weixin.element.public import Get_Cash
from testfarm.test_program.conf.decorator import testcase, setup, teardown
from testfarm.test_program.app.student.login.object_page.login_page import LoginPage
from testfarm.test_program.app.weixin.element.my_account_page import MyAccountPage
from testfarm.test_program.app.weixin.element.opr_web import OprWeb

class Set_offer(unittest.TestCase):
    """我的账户 退出-登陆 操作"""

    @classmethod
    @setup
    def setUp(cls):
        """启动应用"""
        cls.home = HomePage()
        cls.login_page = LoginPage()
        cls.master_page = MasterPage()
        cls.public = Get_Cash()
        cls.my_account = MyAccountPage()
    @classmethod
    @teardown
    def tearDown(cls):
        pass

    @testcase
    def test_case(self):
        self.public.enter_wxzx()
        self.login()
        # self.home.account_management()
        # self.home.click_my_account() # 进入我的账号
        # if self.my_account.wait_my_account_page():
        info = self.my_account.get_info()
        self.change_nickname(info=info)
        self.change_nickname(info=info,type='ensure')
        self.quit_login()
        self.login()
        self.public.quit()
        # else:
        #     print('❌error:进入页面失败')

    def change_nickname(self,info,type='cancel'):
        self.my_account.click_name()
        new_name = self.my_account.input_name()
        if type == 'cancel':
            self.my_account.click_cancel()
            info_after = self.my_account.get_info()
            if info[0] == info_after[0]:
                print('✅账号修改取消功能正常')
            else:
                print('❌error:账号修改取消功能异常，请进行检查，修改前：%s，修改后：%s'%(info[0],info_after[0]))
        elif type == 'ensure':
            self.my_account.click_ensure()
            info_after = self.my_account.get_info()
            if info[0] == info_after[0]:
                print('❌error:名称修改不成功，请进行检查')
            elif info[0] != info_after[0] and info_after[0] == new_name:
                print('✅名称修改成功')
            self.my_account.click_bind_success_ensure()

    def quit_login(self):
        self.my_account.click_quit()
        self.my_account.click_quit_cancel()
        self.my_account.click_quit()
        self.my_account.click_quit_ensure()

    def login(self,phone_number='18955555555'):
        self.home.account_management()
        self.home.click_my_account()
        if self.my_account.wait_bind_page():
            phone_number = self.my_account.input_username(phone_number=phone_number)
            self.my_account.click_get_verification()
            # 调用管理端 获取验证码
            manage = OprWeb(type={'department':'market','opr_type':5},phone=phone_number,code=('school','bind'))
            manage.management_login()
            verification = manage.get_info()
            self.my_account.input_verification(verification)
            self.my_account.click_bind_login()
            self.my_account.click_bind_success_ensure()
            self.home.account_management()
            self.home.click_my_account()
            if self.my_account.wait_my_account_page():
                print('✅登陆成功')
            else:
                print('❌error:登陆失败，请进行检查')