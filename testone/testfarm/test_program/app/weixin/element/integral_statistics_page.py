from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from testfarm.test_program.conf.decorator import teststep,teststeps
from testfarm.test_program.conf.basepage import BasePage
from testfarm.test_program.utils.click_bounds import click_bounds
import datetime, calendar, time

class Integral_Statistics(BasePage):
    @teststeps
    def wait_help_page(self):
        try:
            ele = (By.XPATH, '//*[@text="我就想对比看某几条数据，怎么办？"]')
            WebDriverWait(self.driver, 15, 0.5).until(EC.presence_of_element_located(ele))
            return True
        except:
            return False

    @teststep
    def click_school(self):
        self.driver.find_element_by_xpath('//*[@text="小玉5.21测试"]').click()
        print('点击学校 选择学校')
        time.sleep(0.5)

    @teststep
    def click_school_ensure(self):
        self.driver.find_element_by_xpath('//*[@text="确定"]').click()
        print('点击 学校确认')
        time.sleep(1)

    @teststep
    def click_time(self):
        self.driver.find_element_by_xpath('//*[@text="上上周"]').click()
        print('点击选择时间')
        time.sleep(1)

    @teststep
    def click_next_type(self):
        click_bounds(self,550,1785)
        print('点击下一个类型')
        time.sleep(1)

    @teststep
    def click_type(self):
        self.driver.find_element_by_xpath('//*[@text="学生数量"]').click()
        print('点击选择查看的数量')
        time.sleep(1)

    @teststep
    def click_ensure(self):
        click_bounds(self,985,1250)
        print('点击 确定')

    @teststep
    def click_cancel(self):
        click_bounds(self,95,1250)
        print('点击 取消')

    @teststep
    def click_help(self):
        self.driver.find_element_by_xpath('//*[@text=""]').click()
        print('点击 问号')
        time.sleep(2)

    @teststep
    def click_back(self):
        self.driver.find_element_by_xpath('//*[@resource-id="com.tencent.mm:id/jc"]').click()
        print('点击X号返回')
        time.sleep(2)

    @teststep
    def click_quit(self):
        # self.driver.find_element_by_xpath('//*[@resource-id="android:id/text1"]').click()
        click_bounds(self, 36, 96)
        print('点击<号返回')
        time.sleep(1)

    @teststep
    def get_time(self):
        info = self.driver.find_element_by_xpath('//android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.view.ViewGroup[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[2]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.webkit.WebView[1]/android.webkit.WebView[1]/android.view.View[1]/android.view.View[2]').text
        return info

    @teststep
    def get_type(self):
        info = self.driver.find_element_by_xpath('//android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.view.ViewGroup[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[2]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.webkit.WebView[1]/android.webkit.WebView[1]/android.view.View[1]/android.view.View[3]').text
        return info