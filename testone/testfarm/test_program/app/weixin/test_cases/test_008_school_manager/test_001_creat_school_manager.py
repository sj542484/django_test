import unittest,time
from testfarm.test_program.app.weixin.element.main_page import HomePage
from testfarm.test_program.app.weixin.element.master_page import MasterPage
from testfarm.test_program.conf.decorator import testcase, setup, teardown
from testfarm.test_program.app.student.login.object_page.login_page import LoginPage
from testfarm.test_program.app.weixin.element.statement_page import Statement
from testfarm.test_program.app.weixin.element.public import Get_Cash
from testfarm.test_program.app.weixin.element.school_manager_page import SchoolManagerPage
from testfarm.test_program.app.weixin.test_data.school_name import schoolManagerInfoError,schoolManagerInfoMany
from testfarm.test_program.app.weixin.element.school_proxy_sale_page import SchoolProxySalePage
from testfarm.test_program.app.weixin.element.my_account_page import MyAccountPage

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
        cls.public = Get_Cash()
        cls.sch_manager = SchoolManagerPage()
        cls.school_proxy = SchoolProxySalePage()
        cls.my_account = MyAccountPage()

    @classmethod
    @teardown
    def tearDown(cls):
        pass
    @testcase
    def test_student_bill_error(self):
        self.public.enter_wxzx()
        self.home.account_management()# 点击进入账户管理
        self.home.click_my_school() # 点击进入我的学校
        if self.statement_page.wait_check_page():
            self.sch_manager.click_sch_manager()
            if self.sch_manager.wait_school_manager_page():
                info = self.sch_manager.get_tips()
                self.judge_have_no(info)
                self.sch_manager.click_creat_school_manager()
                if self.sch_manager.wait_privew_page():
                    self.sch_manager.get_tips_in_page()
                    self.judge_out_of_limit() # 输入11名校管并进行判断
                    self.judge_account() # 输入含有正确和错误的校管并进行修改
                    self.master_page.go_back()
                    self.home.account_management()
                    self.home.click_my_account()
                    if self.my_account.wait_my_account_page():
                        time.sleep(5)
                        self.quit_login()
                        self.public.regist_login(phone_number='13233333331') # 登陆校管
                        time.sleep(5)
                        self.have_no_manager()
                        self.have_no_all_account()
                        self.master_page.go_back()
                        self.home.account_management()
                        self.home.click_my_account()
                        if self.my_account.wait_my_account_page():
                            self.quit_login() # 退出校管登陆
                            self.master_page.get_btn()  # 点击返回
                            time.sleep(0.4)
                            self.master_page.go_back()  # 点击返回
                            time.sleep(0.4)
                            if self.login_page.wait_check_page_index():
                                self.login_page.click_weixin()
                                self.public.enter_wxzx()
                                self.public.regist_login()
                                self.home.account_management()
                                self.home.click_my_school()
                                if self.statement_page.wait_check_page():
                                    self.sch_manager.click_sch_manager()
                                    if self.sch_manager.wait_school_manager_page():
                                        self.del_opr()
                                        self.public.quit()
                                    else:
                                        print('❌error:进入页面失败，请进行检查')
                                else:
                                    print('❌error:进入页面失败，请进行检查')
                            else:
                                print('❌error:进入页面失败，请进行检查')
                    else:
                        print('❌error:进入页面错误，请进行检查')
                else:
                    print('❌error:进入页面错误，请进行检查')
            else:
                print('❌error:进入页面错误，请进行检查')
        else:
            print('❌error:进入页面错误，请进行检查')
        print('=====脚本执行完毕=====')

    def judge_out_of_limit(self):
        self.sch_manager.input_info('\n'.join([' '.join(i[:2]) for i in schoolManagerInfoMany]))
        self.sch_manager.click_preview()
        self.sch_manager.click_creat_manager()
        info = self.sch_manager.get_tips()
        self.judge_account_info(info, '最多10名校管')
        time.sleep(3)
        self.master_page.go_back_down()

    def judge_account(self):
        time.sleep(2)
        self.sch_manager.input_info('\n'.join([' '.join(i[:2]) for i in schoolManagerInfoError]))
        self.sch_manager.click_preview()
        info = self.sch_manager.get_tips()
        self.judge_account_info(info, schoolManagerInfoError[0][2])
        self.sch_manager.click_warning_first()
        info = self.sch_manager.get_tips()
        self.judge_account_info(info, schoolManagerInfoError[0][2])
        self.sch_manager.modify_info_name()
        self.sch_manager.click_creat_manager()
        info = self.sch_manager.get_tips()
        self.judge_account_info(info, schoolManagerInfoError[1][2])
        self.sch_manager.modify_info_phone()
        self.sch_manager.click_creat_manager()
        info = self.sch_manager.get_tips()
        self.judge_account_info(info, schoolManagerInfoError[2][2])
        self.sch_manager.modify_info_last_phone()
        self.sch_manager.click_creat_manager()

    def del_manager(self,ele_list):
        for i in range(len(ele_list)):
            self.sch_manager.click_first_manager()
            if i == 0:
                self.sch_manager.click_frozen()
                self.school_proxy.input_pwd().send_keys('123321')
                self.judge_pwd_hide('••••••')
                self.school_proxy.click_hide()
                self.judge_pwd_hide('123321')
                self.school_proxy.click_ensure()
            else:
                self.sch_manager.click_frozen()
            self.sch_manager.click_unbind()
            self.school_proxy.input_pwd().send_keys('123321')
            self.judge_pwd_hide('••••••')
            self.school_proxy.click_hide()
            self.judge_pwd_hide('123321')
            self.school_proxy.click_ensure()
            time.sleep(1.5)

    def judge_manager_num(self):
        num = self.sch_manager.get_school_manager_num()
        if num == len(schoolManagerInfoError):
            print('✅校管设置数量正常')
        else:
            print('❌error:校管数量异常，请进行检查,实际:%s,预计:%s' % (num, len(schoolManagerInfoError)))

    def judge_set_success(self,info_list,page_info):
        get_info = [i.replace('（', ' ').replace('）', '').split(' ') for i in info_list[3::2]]
        tea_info = [j for i in get_info for j in i]
        for i in tea_info:
            if i not in str(page_info):
                print('❌error:添加信息与显示信息不一致，请进行检查，添加信息：%s,页面显示：%s'%(i,page_info))
                break
            else:
                if i == tea_info[-1]:
                    print('✅添加数据与显示数据一致，正常')

    def judge_have_no(self,info):
        if info == '您还没有设置校管':
            print('✅没有校管，进入界面提示正常')
        else:
            print('❌error:没有校管，进入界面提示异常，请进行检查。',info)

    def quit(self):
        self.master_page.go_back()  # 点击返回回到公众号主页面
        self.master_page.get_btn()  # 点击返回
        self.master_page.go_back()  # 点击返回
        if self.login_page.wait_check_page_index():
            self.login_page.click_weixin()
        else:
            print('❌error：进入页面错误')

    def judge_pwd_hide(self,content):
        if self.school_proxy.input_pwd(text=content).text == content:
            print('✅显示/隐藏密码功能正常')
        else:
            print('❌error:显示/隐藏密码功能异常，请进行检查')

    def judge_account_info(self,info,tips):
        if info == tips:
            print('✅实际提示语与期待提示语一致，tips:%s'%tips)
        else:
            print('❌error:实际提示语与期待提示语不一致，实际：%s，期待：%s'%(info,tips))

    def del_opr(self):
        info_list = self.sch_manager.get_success_info()
        self.judge_manager_num()  # 判断显示的校管适量是否正常
        ele_list, page_info = self.sch_manager.get_school_manager_info()
        self.judge_set_success(info_list, page_info)
        self.del_manager(ele_list)
        ele_list = self.sch_manager.get_school_manager_info()[0]
        if len(ele_list) == 0:
            print('✅解除完毕')
        else:
            print('❌error:解除绑定异常，请进行检查')

    def quit_login(self):
        self.my_account.click_quit()
        self.my_account.click_quit_cancel()
        self.my_account.click_quit()
        self.my_account.click_quit_ensure()

    def show_manager(self):
        self.home.account_management()
        self.home.click_my_account()
        if self.my_account.wait_my_account_page():
            info = self.my_account.get_info()
            if info[-1] == '校管':
                print('✅校管身份正常')
            else:
                print('❌error:身份显示错误，预计为：校管，实际为：%s'%info[-1])

    def have_no_manager(self):
        self.home.account_management()
        self.home.click_my_school()
        if self.statement_page.wait_check_page():
            page = self.login_page.page_source()
            if '学校管理员（校管）'in page and '新建学校管理员' not in page:
                print('❌error:学校管理员 & 新建学校管理员 已然存在于页面当中，请进行检查')
            else:
                print('✅管理员界面，不存在学校管理员选项 & 新建学校管理员，正常')
        else:
            print('❌error:进入页面错误，请进行检查')
        time.sleep(1)

    def have_no_all_account(self):
        self.statement_page.click_enter_bill()
        page = self.statement_page.page_source()
        if '本月购卡总额' not in page:
            print('✅校管登陆，本月购卡总额已经不显示，正常')
        else:
            print('❌error:校管登陆，页面中含有 本月购卡总额，请进行检查')
        time.sleep(1)