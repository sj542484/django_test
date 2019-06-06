import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from testfarm.test_program.conf.decorator import teststep
from testfarm.test_program.conf.basepage import BasePage

class Library(BasePage):
    '''付款界面'''
    @teststep
    def wait_check_page(self):
        locator = (By.XPATH, '//*[@resource-id="android:id/text1"]')
        try:
            WebDriverWait(self.driver, 20, 0.5).until(lambda x: x.find_element(*locator))
            return True
        except:
            return False

    @teststep
    def click_library(self):
        self.driver.find_element_by_xpath('//*[@text="本校图书馆"]').click()

    @teststep
    def click_wenhao(self):
        self.driver.find_element_by_xpath('//*[@resource-id="app"]/android.view.View[4]/android.widget.Image[1]').click()

    @teststep
    def click_known(self):
        self.driver.find_element_by_xpath('//android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.view.ViewGroup[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[2]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.webkit.WebView[1]/android.webkit.WebView[1]/android.view.View[1]/android.view.View[8]/android.view.View[4]').click()

    @teststep
    def get_tips_info(self):
        ele = self.driver.find_elements_by_xpath('//android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.view.ViewGroup[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[2]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/com.tencent.tbs.core.webkit.WebView[1]/android.webkit.WebView[1]/android.view.View[1]/android.view.View[8]/android.view.View')
        info = [i.text for i in ele]
        print('\n'.join(info))

    @teststep
    def get_active_tea(self):
        '''获取管理员信息'''
        ele = self.driver.find_elements_by_xpath('//android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.view.ViewGroup[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[2]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/com.tencent.tbs.core.webkit.WebView[1]/android.webkit.WebView[1]/android.view.View[1]/android.view.View[5]/android.view.View[2]//android.view.View')
        info = [i.text for i in ele]
        return info

    @teststep
    def click_modify(self):
        self.driver.find_element_by_xpath('//*[@text="更换"]').click()
        print('点击 更换')

    @teststep
    def get_Instruction(self):
        '''获取 图书馆界面说明信息'''
        ele = self.driver.find_element_by_xpath('//android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.view.ViewGroup[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[2]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/com.tencent.tbs.core.webkit.WebView[1]/android.webkit.WebView[1]/android.view.View[1]/android.view.View[6]/android.view.View')
        info = [i.text for i in ele]
        print('\n'.join(info))

    @teststep
    def get_all_tea_info(self):
        ele = self.driver.find_elements_by_xpath('//android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.view.ViewGroup[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[2]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/com.tencent.tbs.core.webkit.WebView[1]/android.webkit.WebView[1]/android.view.View[1]/android.view.View[8]//android.view.View')
        info = [i.text for i in ele]
        print(info,'============')
        print('\n'.join(info))
        return ele,info

    @teststep
    def choose_tea(self,tea_ele,index):
        '''
        :param tea_ele: 老师对象列表
        :param index: 选择第index个老师
        :return:
        '''
        tea_ele[index].click()

    @teststep
    def choose_ok(self):
        self.driver.find_element_by_xpath('//*[@text="选好啦"]').click()