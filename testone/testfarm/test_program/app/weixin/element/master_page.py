import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from testfarm.test_program.conf.decorator import teststep, teststeps
from testfarm.test_program.conf.basepage import BasePage
from testfarm.test_program.utils.click_bounds import click_bounds


class MasterPage(BasePage):

    @teststeps
    def set_price(self):
        # 点击设置优惠价
        time.sleep(2)
        self.driver.find_element_by_xpath('//*[@text="设置优惠价"]').click()
        print("进入设置优惠价页面")

    @teststeps
    def wait_set_page(self):
        locator = (By.XPATH, '//*[@resource-id="app"]/android.view.View[2]')
        try:
            WebDriverWait(self.driver, 10, 0.3).until(lambda x: x.find_element(*locator))
            return True
        except:
            return False

    @teststeps
    def click_set_half(self):
        self.driver.find_element_by_xpath('//*[@resource-id="app"]/android.view.View[5]/android.view.View[3]/android.view.View[2]/android.view.View[1]').click()
        time.sleep(1)
        print('点击半年卡设置')

    @teststep
    def click_set_year(self):
        self.driver.find_element_by_xpath('//*[@resource-id="app"]/android.view.View[6]/android.view.View[3]/android.view.View[2]/android.view.View[1]').click()
        time.sleep(1)
        print('点击年卡设置')

    @teststeps
    def set_password(self):
        # 点击设置按钮
        self.driver.find_element_by_xpath('//*[@text="请输入密码"]').send_keys("123321")
        print("输入密码******！")
        time.sleep(1)

    @teststeps
    def click_determine(self):
        # 点击确定按钮
        # self.driver.find_element_by_xpath('//*[@text="确定"]').click()
        click_bounds(self,750,840)
        print('确定')
        time.sleep(2)

    @teststeps
    def click_again_determine(self):
        # 点击确定按钮
        self.driver.find_element_by_xpath('//android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.view.ViewGroup[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[2]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.webkit.WebView[1]/android.webkit.WebView[1]/android.view.View[1]/android.view.View[10]/android.view.View[5]/android.view.View[2]').click()
        print('点击确定')
        time.sleep(2)

    def click_immediately_buy(self):
        '''点击立即购买'''
        time.sleep(1)
        click_bounds(self,700,1950)
        print('点击立即购买')

    @teststep
    def click_team_buy(self):
        self.driver.find_element_by_xpath('//android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.view.ViewGroup[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[2]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.webkit.WebView[1]/android.webkit.WebView[1]/android.view.View[1]/android.view.View[1]/android.view.View[1]/android.view.View[1]/android.view.View[3]/android.view.View[1]/android.view.View[6]/android.view.View[5]/android.view.View[2]').click()
        print('点击 团购')

    def hide_keyboard(self):
        # 隐藏软键盘
        self.driver.hide_keyboard()

    @teststeps
    def go_back(self):
        # 点击返回回到公主号主页面
        self.driver.find_element_by_xpath('//*[@resource-id="com.tencent.mm:id/kb"]').click()
        print('点击X返回')
        time.sleep(2)

    def go_back_down(self):
        self.driver.find_element_by_xpath('//*[@resource-id="app"]/android.view.View[1]').click()
        # click_bounds(self,65,280)
        print('点击返回<')
        time.sleep(0.5)

    def click_x(self):
        # 点击x结束购买协议
        self.driver.find_element_by_xpath('//*[@text=""]').click()
        print("点击x结束购买协议")

    def click_my_avatar(self):
        # 点击我的头像
        time.sleep(1)
        self.driver.find_element_by_xpath('//*[@text="大雄"]').click()
        print("点击我的头像进入聊天对话框")
        time.sleep(2)

    @teststeps
    def get_btn(self):
        # 点击返回
        print("返回微信主页面")
        self.driver.find_element_by_xpath('//*[@resource-id="com.tencent.mm:id/k1"]').click()
        time.sleep(2)

    @teststeps
    def set_normal_price(self):
        # 设置正常价格
        time.sleep(1)
        self.driver.find_element_by_xpath('//android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.view.ViewGroup[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[2]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.webkit.WebView[1]/android.webkit.WebView[1]/android.view.View[1]/android.view.View[10]/android.view.View[4]/android.widget.EditText[1]').send_keys('99')
        return '99'

    @teststep
    def share_card(self):
        self.driver.find_element_by_xpath('//*[@text="分享优惠页"]').click()
        time.sleep(1)

    @teststep
    def click_more(self):
        self.driver.find_element_by_xpath('//*[@resource-id="com.tencent.mm:id/jy"]').click()
        time.sleep(1)

    @teststep
    def click_share_friend(self):
        self.driver.find_element_by_xpath('//*[@text="发送给朋友"]').click()
        time.sleep(1)

    @teststep
    def click_myself(self):
        self.driver.find_element_by_xpath('//*[@text="大雄"]').click()
        time.sleep(1)

    @teststep
    def click_send(self):
        self.driver.find_element_by_xpath('//*[@resource-id="com.tencent.mm:id/az_"]').click()
        time.sleep(1)

    @teststep
    def long_press(self):
        pass