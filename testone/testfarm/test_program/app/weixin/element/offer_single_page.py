import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from testfarm.test_program.conf.decorator import teststep, teststeps
from testfarm.test_program.conf.basepage import BasePage
from testfarm.test_program.utils.click_bounds import click_bounds


class Offer_single(BasePage):
    '''付款界面'''
    @teststep
    def wait_check_card_page(self):
        locator = (By.XPATH, '//*[@resource-id="android:id/text1"]')
        try:
            WebDriverWait(self.driver, 20, 0.5).until(lambda x: x.find_element(*locator))
            return True
        except:
            return False

    @teststep
    def wait_team_buy_page(self):
        """以“title:重置密码”的xpath @text为依据"""
        locator = (By.XPATH, '//*[@text="拼团须知"]')
        try:
            WebDriverWait(self.driver, 20, 0.3).until(lambda x: x.find_element(*locator))
            return True
        except:
            return False

    @teststep
    def wait_invalid_page(self):
        '''失效页面'''
        locator = (By.XPATH, '//*[@text="活动失效啦，去看看别的活动吧"]')
        try:
            WebDriverWait(self.driver, 20, 0.5).until(lambda x: x.find_element(*locator))
            return True
        except:
            return False

    def input_pwd(self):
        # 重新输入学生的密码
        ele = self.driver.find_element_by_xpath('//*[@text="学生密码"]/following-sibling::android.view.View[1]/android.widget.EditText')
        return ele

    def input_phone(self):
        # 显示手机号为空的情况
        ele = self.driver.find_element_by_xpath('//android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.view.ViewGroup[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[2]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.webkit.WebView[1]/android.webkit.WebView[1]/android.view.View[1]/android.view.View[4]/android.view.View[2]/android.view.View[2]/android.widget.EditText[1]')
        return ele

    def click_discount_card(self):
        # 点击分享优惠卡
        time.sleep(2)
        ele = self.driver.find_element_by_xpath('//*[@resource-id="com.tencent.mm:id/ap_"]')
        return ele

    @teststep
    def wait_check_page(self):
        """以“title:重置密码”的xpath @text为依据"""
        locator = (By.XPATH, '//*[@text="请输入手机号"]')
        try:
            WebDriverWait(self.driver, 20, 0.5).until(lambda x: x.find_element(*locator))
            return True
        except:
            return False

    def click_buy_agument(self):
        # 点击购买协议
        self.driver.find_element_by_xpath('//*[@text="《购买协议》"]').click()
        # click_bounds(self, 625, 1200)
        time.sleep(2)
        print("显示购买协议")

    def click_now_buy(self):
        time.sleep(5)
        # 点击立即支付
        click_bounds(self, 830, 1950)
        print('点击立即支付')
        time.sleep(3)

    def ensure_buy(self):
        time.sleep(1)
        self.driver.find_element_by_xpath('//*[@resource-id="com.tencent.mm:id/f9y"]').click()
        print('确认支付')
        time.sleep(1)

    def click_ensure(self):
        ele = self.driver.find_element_by_xpath('//*[@text="确定"]')
        return ele

    def click_ensure_cancel_trade(self):
        self.driver.find_element_by_xpath('//*[@resource-id="com.tencent.mm:id/az_"]').click()
        print('点击 确认取消交易')

    @teststep
    def get_tips(self,tip):
        tip = self.driver.find_element_by_xpath('//*[@text="{}"]'.format(tip)).text
        return tip

    @teststep
    def get_card_ele(self):
        ele_list = self.driver.find_elements_by_xpath(
            '//android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.view.ViewGroup[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[2]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.webkit.WebView[1]/android.webkit.WebView[1]/android.view.View[1]/android.view.View[1]/android.view.View[1]/android.view.View[1]/android.view.View'
        )[1:]
        return ele_list

    @teststep
    def get_card_info(self):
        '''获取页面优惠卡信息'''
        ele_list = self.get_card_ele()
        info_lists = []
        for i in range(len(ele_list)):
            ele_lists = self.driver.find_elements_by_xpath('//android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.view.ViewGroup[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[2]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.webkit.WebView[1]/android.webkit.WebView[1]/android.view.View[1]/android.view.View[1]/android.view.View[1]/android.view.View[1]/android.view.View[%d]/android.view.View[1]/android.view.View'%(i + 2))
            ele_info = [j.text for j in ele_lists]
            info_lists.append(ele_info)
        return info_lists

    @teststep
    def judge_card(self,card_price,card_type,card_info):
        if card_type == '半年卡':
            if len(card_info) == 1:
                if card_info[0][0] == '半年卡' and card_info[0][1] == '(183天)' and card_info[0][2] == '优惠价￥ %s'%card_price and card_info[0][4] == '原价￥ 183':
                    print('✅半年卡设置成功')
                else:
                    print('❌error:半年卡设置失败，页面信息为：%s,设置价格为：%s'%(card_info,card_price))
            else:
                print('❌error:卡片数量存在问题，请进行检查')
        elif card_type == '年卡':
            if len(card_info) == 2:
                if card_info[1][0] == '年卡' and card_info[1][1] == '(365天)' and card_info[1][2] == '优惠价￥ %s'%card_price and card_info[1][4] == '原价￥ 365':
                    print('✅年卡设置成功')
                else:
                    print('❌error:年卡设置失败，页面信息为：%s,设置价格为：%s'%(card_info,card_price))

    @teststep
    def get_team_page_title(self):
        '''获取页面titile'''
        res = self.driver.find_element_by_xpath('//*[@resource-id="android:id/text1"]').text
        if res == '5.21-在线助教年卡优惠':
            print('✅以显示学校简称-在线助教年卡优惠活动')
        else:
            print('❌error:页面title显示存在问题，请进行检查，显示为：%s'%res)

    @teststep
    def get_team_page_card_info(self,price):
        '''获取优惠卡的信息，类型，价格'''
        ele_list = self.driver.find_elements_by_xpath('//android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.view.ViewGroup[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[2]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.webkit.WebView[1]/android.webkit.WebView[1]/android.view.View[1]/android.view.View[1]/android.view.View[1]/android.view.View[1]/android.view.View[2]/android.view.View')
        info_list = [i.text for i in ele_list[:-1]]
        print(info_list)
        if str(price) in info_list[1]:
            print('✅优惠价价格正确')
        else:
            print('❌error:优惠券价格异常，请进行检查，设置为：%s,实际为：%s'%(price,info_list[1]))

    @teststep
    def get_team_buy_knows(self):
        '''获取拼团须知，并点击'''
        ele_list = self.driver.find_elements_by_xpath('//android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.view.ViewGroup[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[2]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.webkit.WebView[1]/android.webkit.WebView[1]/android.view.View[1]/android.view.View[1]/android.view.View[1]/android.view.View[1]/android.view.View[3]/android.view.View')
        info_list = [i.text for i in ele_list]
        print('：'.join(info_list))
        ele_list[1].click()
        time.sleep(1)

    @teststep
    def get_team_buy_tips(self):
        ele_list = self.driver.find_elements_by_xpath('//android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.view.ViewGroup[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[2]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.webkit.WebView[1]/android.webkit.WebView[1]/android.view.View[2]/android.view.View[2]/android.widget.ListView[1]/android.view.View')
        info_list = [[j.text for j in  i.find_elements_by_xpath('./android.view.View')] for i in ele_list]
        print(info_list)

    @teststep
    def click_team_buy_tips_know(self):
        self.driver.find_element_by_xpath('//android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.view.ViewGroup[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[2]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.webkit.WebView[1]/android.webkit.WebView[1]/android.view.View[2]/android.view.View[2]/android.view.View[2]/android.view.View[1]').click()
        time.sleep(1)

    @teststep
    def get_team_rule(self):
        ele_list = self.driver.find_elements_by_xpath('//android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.view.ViewGroup[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[2]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.webkit.WebView[1]/android.webkit.WebView[1]/android.view.View[1]/android.view.View[1]/android.view.View[1]/android.view.View[1]/android.widget.ListView[1]/android.view.View')
        info_list = [i.text for i in ele_list]
        print(info_list)

    @teststep
    def click_open_group(self,price):
        ele_list = self.driver.find_elements_by_xpath('//android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.view.ViewGroup[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[2]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.webkit.WebView[1]/android.webkit.WebView[1]/android.view.View[1]/android.view.View[1]/android.view.View[3]/android.view.View')
        info_list = [i.text for i in ele_list]
        if str(price) in info_list[0]:
            print('✅拼团价格显示正确')
        else:
            print('❌error:拼团价格显示异常，请进行检查，设置为：%s,实际为：%s'%(price,info_list[0]))
        ele_list[0].click()
        time.sleep(3)

    @teststep
    def team_input_phone(self):
        time.sleep(2)
        ele = self.driver.find_element_by_xpath('//*[@text="学生账号"]/following-sibling::android.view.View[1]/android.widget.EditText')
        return ele

    @teststep
    def team_input_pwd(self):
        time.sleep(2)
        ele = self.driver.find_element_by_xpath('//*[@text="学生密码"]/following-sibling::android.view.View[1]/android.widget.EditText')
        return ele

    @teststep
    def del_share_link(self):
        self.driver.find_element_by_xpath('//*[@text="删除"]').click()
        time.sleep(1)

    @teststep
    def del_ensure(self):
        self.driver.find_element_by_xpath('//*[@resource-id="com.tencent.mm:id/az_"]').click()