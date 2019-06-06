import datetime,time,pymysql
from testfarm.test_program.app.weixin.element.main_page import HomePage
from testfarm.test_program.app.weixin.element.master_page import MasterPage
from testfarm.test_program.app.weixin.test_cases.login_page import Loginpage
from testfarm.test_program.conf.decorator import testcase
from testfarm.test_program.conf.basepage import BasePage

from testfarm.test_program.app.weixin.test_data.phone_list import student_buy_data
from testfarm.test_program.app.weixin.element.offer_single_page import Offer_single
from testfarm.test_program.app.student.login.object_page.login_page import LoginPage
from testfarm.test_program.app.weixin.element.statement_page import Statement
from appium.webdriver.common.touch_action import TouchAction
from testfarm.test_program.app.weixin.element.my_account_page import MyAccountPage
from testfarm.test_program.app.weixin.element.opr_web import OprWeb


class Get_Cash(BasePage):
    """对账单页面的信息"""
    def __init__(self):
        """启动应用"""
        self.home = HomePage()
        self.login_page = LoginPage()
        self.master_page = MasterPage()
        self.login = Loginpage()
        self.statement_page = Statement()
        self.offer_page = Offer_single()
        self.my_account = MyAccountPage()

    def enter_wxzx(self):
        '''进入公众号首页'''
        self.login_page.weixin_app()  # 判断APP当前状态
        self.login_page.clear_kernel()
        time.sleep(1)
        if self.login_page.wait_check_main_page():
            self.home.click_contacts()  # 进入通讯录
            self.home.click_public()  # 进入公众号
            self.home.click_start()  # 进入万星在线
            print("进入万星在线成功")
        else:
            print('❌error:进入微信首页失败，请进行检查')

    def enter_friend(self,statue='click'):
        '''进入好友 进入分享链接'''
        self.login_page.weixin_app()  # 判断APP当前状态
        self.login_page.clear_kernel()
        self.login_page.click_weixin()  # 点击微信
        self.master_page.click_my_avatar()  # 点击我的头像
        if statue == 'click':
            self.offer_page.click_discount_card().click()  # 点击我的优惠卡
            print("点击聊天框中的我的优惠卡")
            print("进入优惠页界面")
        else:
            actions = TouchAction(self.driver)
            actions.long_press(self.offer_page.click_discount_card())
            actions.perform()
            self.offer_page.del_share_link()
            self.offer_page.del_ensure()
            self.master_page.get_btn()
            print('✅长按连接，删除正常')
        time.sleep(4)

    @testcase
    def test_num_all(self):
        '''
        :return: 总额，余额，学校账单第一条信息，总账单数量
        '''
        if self.statement_page.wait_check_page():
            self.statement_page.click_statement() #进入对账单
            if self.statement_page.show_statement_num_wait():
                total_cash = self.statement_page.show_month_price() # 显示本月总额
                school_remaining = self.statement_page.show_school_money() # 学校余额是多少
                self.statement_page.click_enter_bill()
                if self.statement_page.judge_enter_bill():
                    first_order_info = self.statement_page.get_first_order()
                    all_order_num = self.statement_page.get_all_order()
                    self.master_page.go_back_down()  # 点击返回
                    self.master_page.go_back_down()  # 点击返回
                    return total_cash,school_remaining,first_order_info,len(all_order_num)
                else:
                    print('❌error:进入页面失败，请进行检查')
            else:
                print('❌error:进入页面失败，请进行检查')
        else:
            print('❌error:进入页面失败，请进行检查')

    def school_info(self, before_info, after_info, peo_num = -1, unit_price = 15,opr_type = '代买'):
        '''学校订单确认'''
        print('after_info:',after_info)
        print('before_info:',before_info)
        print('peo_num:',peo_num,'unit_price:',unit_price,'opr_type:',opr_type)
        today = datetime.date.today().strftime('%m-%d')
        if opr_type == '代买':
            data = '{} 人 月卡 (31天)'.format(peo_num)
            plus_minus = '-'
        elif opr_type == '代退':
            data = '代退 Saiyaren123(17666666666) 31 天'
            plus_minus = ''
        if after_info[0] == before_info[0]:
            if before_info[1] - after_info[1] == peo_num * unit_price:
                if after_info[3] - before_info[3] == 1:
                    if after_info[2][0] == '\xa0{}\xa0'.format(opr_type)\
                        and after_info[2][1] == '\xa0{}￥{}\xa0'.format(plus_minus,abs(peo_num) * unit_price)\
                            and after_info[2][2] == '{} \xa0\xa0 {}'.format(today,data):
                                print('✅订单完成，校长端购款总额正确，学校余额正确，学校账单添加成功')
                    else:
                        print('❌error:订单信息异常，请进行检查，%s'%after_info[2])
                else:
                    print('❌error:学校账单添加失败，请进行检查')
            else:
                print('❌error:学校余额异常，请进行检查，before:%s,after:%s'%(before_info[1],after_info[1]))
        else:
            print('❌error:购款总额异常，请进行检查，before:%s,after:%s'%(before_info[0],after_info[0]))

    def search_verification(self,input_ele,data,ensure_ele):
        '''输入框输入 最后一组为正确的输入'''
        for i in data[:-1]:
            print(i)
            for index,j in enumerate(input_ele):
                # 循环输入框
                j.send_keys(i[index])
                time.sleep(0.5)
            ensure_ele.click()
            time.sleep(0.5)
            try:
                # 页面顶端的tips
                tips = self.statement_page.get_tips().text
            except:
                # 输入框下方的tips
                tips = self.offer_page.get_tips(i[-1])
            if tips == i[-1]:
                print('✅搜索校验提示正常，输入：%s,tips:%s'%(i[0],tips))
            else:
                print('❌error:搜索校验提示异常，请进行检查，输入：%s,tips:%s'%(i[0],tips))
            time.sleep(2)
        # 最后输入正确的数据 下一步
        for index, j in enumerate(input_ele):
            # 循环输入框
            j.send_keys(data[-1][index])
            time.sleep(0.5)
        ensure_ele.click()
        time.sleep(3)
        return data[-1][0]

    def quit(self):
        '''退出到微信主界面'''
        self.master_page.go_back()  # 点击返回回到公众号主页面
        time.sleep(0.4)
        self.master_page.get_btn()  # 点击返回
        time.sleep(0.4)
        self.master_page.go_back()  # 点击返回
        time.sleep(0.4)
        if self.login_page.wait_check_page_index():
            self.login_page.click_weixin()
        else:
            print('❌error:进入页面失败，请进行检查')

    @testcase
    def single_pay(self,card_price,card_type):
        '''单购'''
        # 进入优惠券
        self.enter_friend()
        # 查看优惠券类型与优惠信息 进行判断
        if self.offer_page.wait_check_card_page():
            card_info = self.offer_page.get_card_info()
            self.offer_page.judge_card(card_price,card_type,card_info)
            # 购买
            self.master_page.click_immediately_buy()  # 点击立即购买
            if self.offer_page.wait_check_page():
                input_stu_ele = self.offer_page.input_phone()
                input_pwd_ele = self.offer_page.input_pwd()
                ele = self.offer_page.click_ensure()
                self.search_verification(input_ele=(input_stu_ele, input_pwd_ele), data=student_buy_data, ensure_ele=ele)  # 手机号输入是这个学校的学生
                self.offer_page.click_buy_agument()  # 点击购买协议
                self.master_page.click_x()
                self.offer_page.click_now_buy()  # 点击支付
                time.sleep(5)
                self.offer_page.ensure_buy()  # 确定支付
                self.master_page.go_back()  # 点击返回
                self.offer_page.click_ensure_cancel_trade()  # 点击确定取消支付
                self.master_page.go_back()  # 返回X
                self.master_page.get_btn()  # 返回 主界面
            else:
                print('❌error:进入页面失败，请进行检查')
        else:
            print('❌error:进入页面失败，请进行检查')

    @testcase
    def team_pay(self,price):
        '''团购'''
        # 进入优惠券
        self.enter_friend()
        # 进行购买操作
        if self.offer_page.wait_check_card_page():
            self.master_page.click_team_buy()  # 点击立即购买
            if self.offer_page.wait_team_buy_page():
                self.offer_page.get_team_page_title()
                self.offer_page.get_team_page_card_info(price)
                self.offer_page.get_team_buy_knows()
                # self.offer_page.get_team_buy_tips()
                self.offer_page.click_team_buy_tips_know()
                # self.offer_page.get_team_rule()
                self.offer_page.click_open_group(price)
                input_stu_ele = self.offer_page.team_input_phone()
                input_pwd_ele = self.offer_page.team_input_pwd()
                ele = self.offer_page.click_ensure()
                self.search_verification(input_ele=(input_stu_ele, input_pwd_ele), data=student_buy_data,
                                                ensure_ele=ele)  # 手机号输入是这个学校的学生
                self.offer_page.click_buy_agument()  # 点击购买协议
                self.master_page.click_x()
                self.offer_page.click_now_buy()  # 点击支付
                time.sleep(5)
                self.offer_page.ensure_buy()  # 确定支付
                self.master_page.go_back()  # 点击返回
                self.offer_page.click_ensure_cancel_trade()  # 点击确定取消支付
                self.master_page.go_back()  # 返回X
                self.master_page.get_btn()  # 返回 主界面
            else:
                print('❌error:进入页面失败，请进行检查')
        else:
            print('❌error:进入页面失败，请进行检查')

    def updata_mysql(self):
        # db = pymysql.connect("172.17.0.200", "developer", "8B#T&Bel", "b_vanthink_core")
        db = pymysql.connect("172.17.0.200", "director", "AZ*vkTJj", "b_vanthink_core")
        sql = "UPDATE user SET wechat_id = '' WHERE phone = 13412345678"
        db.cursor().execute(sql)
        db.commit()
        db.close()
        print('✅op_id清除成功')

    def regist_login(self,phone_number='18955555555'):
        self.home.account_management()
        self.home.click_my_account()
        if self.my_account.wait_bind_page():
            phone_number = self.my_account.input_username(phone_number)
            self.my_account.click_get_verification()
            # 调用管理端 获取验证码
            manage = OprWeb(type={'department': 'market', 'opr_type': 5}, phone=phone_number, code=('school', 'bind'))
            manage.management_login()
            verification = manage.get_info()
            self.my_account.input_verification(verification)
            self.my_account.click_bind_login()
            if self.my_account.wait_set_pwd_page():
                self.my_account.input_pwd()
                self.my_account.input_pwd_again()
                self.my_account.click_set_pwd()
                self.my_account.click_ensure_in_last()
                self.my_account.click_bind_success_ensure()
                print('✅登陆成功')
            else:
                self.my_account.click_bind_success_ensure()

if __name__ == '__main__':
    db = Get_Cash()
    db.updata_mysql()