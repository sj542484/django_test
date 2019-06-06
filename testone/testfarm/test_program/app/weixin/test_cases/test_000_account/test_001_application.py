import time
import unittest
from testfarm.test_program.app.weixin.element.main_page import HomePage
from testfarm.test_program.app.weixin.element.master_page import MasterPage
from testfarm.test_program.app.weixin.element.public import Get_Cash
from testfarm.test_program.conf.decorator import testcase, setup, teardown
from testfarm.test_program.app.student.login.object_page.login_page import LoginPage
from testfarm.test_program.app.weixin.element.my_account_page import MyAccountPage
from testfarm.test_program.app.weixin.element.opr_web import OprWeb
from testfarm.test_program.app.weixin.element.creat_school_page import CreatSchoolPage

class Set_offer(unittest.TestCase):
    """我的账户 退出-申请-登陆操作"""

    @classmethod
    @setup
    def setUp(cls):
        """启动应用"""
        cls.home = HomePage()
        cls.login_page = LoginPage()
        cls.master_page = MasterPage()
        cls.public = Get_Cash()
        cls.my_account = MyAccountPage()
        cls.creat_school = CreatSchoolPage()

    @classmethod
    @teardown
    def tearDown(cls):
        pass

    @testcase
    def test_case(self):
        self.public.enter_wxzx()
        self.home.account_management()
        self.home.click_my_account() # 进入我的账号
        if self.my_account.wait_my_account_page():
            self.quit_login()
            phone = self.application()
            self.public.regist_login(phone_number=phone)
            self.del_school(phone_number=phone)
            self.quit()
        else:
            self.login()
            print('❌error:进入页面失败')

    def application(self):
        self.home.account_management()
        self.home.click_my_account()
        if self.my_account.wait_bind_page():
            self.my_account.click_apply()
            phone = self.my_account.input_all_info()
            self.my_account.click_location()
            self.creat_school.choose_lacation()  # 选择地点
            self.creat_school.click_ensure()  # 点击确定
            self.my_account.apply_click_get_verification()
            manage = OprWeb(type={'department':'market','opr_type':5},phone=phone,code=('school','apply'))
            manage.management_login()
            verification = manage.get_info()
            if verification != '没有获取成功':
                self.my_account.apply_input_verification(verification)
                self.my_account.apply_click_apply()
                manage = OprWeb(type={'department': 'market', 'opr_type': 1}, phone=phone)
                manage.management_login()
                manage.apply_succee(phone)
                self.master_page.go_back()
                return phone
            else:
                print('❌error:验证码获取失败，请进行检查')

    def quit_login(self):
        self.my_account.click_quit()
        self.my_account.click_quit_cancel()
        self.my_account.click_quit()
        self.my_account.click_quit_ensure()

    def login(self,phone_number='18955555555'):
        # self.home.account_management()
        # self.home.click_my_account()
        if self.my_account.wait_bind_page():
            phone_number = self.my_account.input_username(phone_number)
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

    def del_school(self,phone_number):
        manager = OprWeb(type={'department':'market','opr_type':'3'})
        manager.management_login()
        manager.del_school()
        self.public.updata_mysql()

    def quit(self):
        self.master_page.go_back()  # 点击返回回到公众号主页面
        time.sleep(0.4)
        self.master_page.get_btn()  # 点击返回
        time.sleep(0.4)
        if self.login_page.wait_check_page_index():
            self.login_page.click_weixin()
        else:
            print('❌error:进入页面失败，请进行检查')