import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from testfarm.test_program.conf.decorator import teststep, teststeps
from testfarm.test_program.conf.basepage import BasePage
from testfarm.test_program.utils.click_bounds import click_bounds


class Year_page(BasePage):
    '''设置年卡页面'''
    @teststeps
    def click_year_cancel(self):
        self.driver.find_element_by_xpath('//android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.view.ViewGroup[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[2]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.webkit.WebView[1]/android.webkit.WebView[1]/android.view.View[1]/android.view.View[6]/android.view.View[3]/android.view.View[2]/android.view.View[2]').click()
        time.sleep(1)

    @teststep
    def click_half_year_cancel(self):
        self.driver.find_element_by_xpath('//android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.view.ViewGroup[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[2]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.webkit.WebView[1]/android.webkit.WebView[1]/android.view.View[1]/android.view.View[5]/android.view.View[3]/android.view.View[2]/android.view.View[2]').click()

    @teststeps
    def set_price_wait(self):
        locator = (By.XPATH,'//android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.view.ViewGroup[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[2]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.webkit.WebView[1]/android.webkit.WebView[1]/android.view.View[1]/android.view.View[10]/android.view.View[4]/android.widget.EditText[1]')
        try:
            WebDriverWait(self.driver, 20, 0.5).until(lambda x: x.find_element(*locator))
            return True
        except:
            return False

    @teststeps
    def set_price(self,price):
        teamPrice = str(price[0])
        singlePrice = str(price[1])
        # 团购价
        self.driver.find_element_by_xpath('//android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.view.ViewGroup[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[2]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.webkit.WebView[1]/android.webkit.WebView[1]/android.view.View[1]/android.view.View[10]/android.view.View[4]/android.widget.EditText[1]').send_keys(teamPrice)
        # 单购价
        time.sleep(0.5)
        self.driver.find_element_by_xpath('//android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.view.ViewGroup[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[2]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.webkit.WebView[1]/android.webkit.WebView[1]/android.view.View[1]/android.view.View[10]/android.view.View[6]/android.widget.EditText[1]').send_keys(singlePrice)

    @teststeps
    def click_ensure(self):
        # 价格输入完成 点击确定
        self.driver.find_element_by_xpath('//android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.view.ViewGroup[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[2]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.webkit.WebView[1]/android.webkit.WebView[1]/android.view.View[1]/android.view.View[10]/android.view.View[8]/android.view.View[2]').click()
        # print('年卡优惠券设置价格输入完成～～点击确定')
        time.sleep(2)

    @teststeps
    def expect_statue(self,price):
        teamPrice = int(price[0])
        singlePrice = int(price[1])
        if teamPrice < 150:
            print('预期结果 年卡优惠价不能低于￥150')
            return '年卡优惠价不能低于￥150'
        elif 150 < teamPrice < 365 and singlePrice < 150:
            print('预期结果 年卡优惠价不能低于￥150')
            return '年卡优惠价不能低于￥150'
        elif 150 < teamPrice < 365 and singlePrice > 365:
            print('预期结果 年卡优惠价不能高于￥365')
            return '年卡优惠价不能高于￥365'
        elif teamPrice > 365 and singlePrice > 150:
            print('预期结果 年卡优惠价不能高于￥365')
            return '年卡优惠价不能高于￥365'
        elif teamPrice > 365 and singlePrice < 150:
            print('预期结果 年卡优惠价不能低于￥150')
            return '年卡优惠价不能低于￥150'
        elif teamPrice > singlePrice:
            print('预期结果 单购价不能低于团购价')
            return '单购价不能低于团购价'
        elif teamPrice == singlePrice:
            print('预期结果 单购价不能与团购价相同')
            return '单购价不能与团购价相同'
        elif teamPrice < singlePrice:
            print('预期结果 价格设置正确')
            return '价格设置正确'

    @teststeps
    def judge_statue(self):
        try:
            ele = self.driver.find_element_by_xpath('//android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.view.ViewGroup[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[2]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.webkit.WebView[1]/android.webkit.WebView[1]/android.view.View[2]').text
            return ele
        except:
            return '价格设置正确'

    @teststeps
    def click_cancel_wait(self):
        locator = (By.XPATH, '//android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.view.ViewGroup[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[2]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.webkit.WebView[1]/android.webkit.WebView[1]/android.view.View[1]/android.view.View[10]/android.view.View[3]/android.view.View[2]')
        try:
            WebDriverWait(self.driver, 10, 0.5).until(lambda x: x.find_element(*locator))
            return True
        except:
            return False

    @teststeps
    def click_cancel(self):
        # 点击取消
        # self.driver.find_element_by_xpath('//*[@text="确定"]').click()
        click_bounds(self,710,1235)
        print('确认取消该优惠')
        time.sleep(1.5)

    @teststeps
    def send_pwd(self):
        # 取消后输入密码
        self.driver.find_element_by_xpath('//*[@text="请输入密码"]').send_keys('123321')
        print('输入密码')
        time.sleep(1)

    @teststep
    def click_determine(self):
        click_bounds(self,720,1300)
        print('点击 确定')

    @teststeps
    def cancel_success_judge(self):
        # 取消成功后判断是否成功
        ele = self.driver.find_element_by_xpath('//*[@resource-id="app"]/android.view.View[6]/android.view.View[3]/android.view.View[3]').text
        if ele == '优惠价：未设置':
            print('✅年卡优惠取消操作成功')
        else:
            print('\n\t❌error:%s,年卡优惠取消操作异常\n'%ele)