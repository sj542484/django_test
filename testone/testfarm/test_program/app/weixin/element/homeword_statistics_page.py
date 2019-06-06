from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from testfarm.test_program.conf.decorator import teststep,teststeps
from testfarm.test_program.conf.basepage import BasePage
from testfarm.test_program.utils.click_bounds import click_bounds
import datetime, calendar, time

class HomeWorkStatistics(BasePage):
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
        print('点击 确定')
        time.sleep(1)

    @teststep
    def click_tea(self):
        # self.driver.find_element_by_xpath('//*[@resource-id="app"]/android.view.View[2]/android.view.View[2]').click()
        click_bounds(self,460,290)
        print('点击全部老师 选择老师')
        time.sleep(2)

    @teststep
    def click_last_weak(self):
        self.driver.find_element_by_xpath('//*[@text="上周"]').click()
        print('点击 上周')
        time.sleep(0.3)

    @teststep
    def click_two_weaks_age(self):
        self.driver.find_element_by_xpath('//*[@text="上上周"]').click()
        # click_bounds(self,230,280)
        print('点击 上上周')

    @teststep
    def click_last_month(self):
        self.driver.find_element_by_xpath('//*[@text="上月"]').click()
        # click_bounds(self,375,280)
        print('点击 上个月')
        # time.sleep(0.5)

    @teststep
    def get_date(self):
        time.sleep(3)
        info_date = self.driver.find_element_by_xpath('//android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.view.ViewGroup[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[2]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.webkit.WebView[1]/android.webkit.WebView[1]/android.view.View[1]/android.view.View[5]/android.view.View[3]').text
        print('获得的时间是：',info_date)
        return info_date.split('-')

    @teststep
    def select_all(self):
        self.driver.find_element_by_xpath('//*[@resource-id="app"]/android.view.View[6]/android.view.View[1]/android.view.View[2]/android.view.View[2]').click()
        print('点击 全选')
        time.sleep(1)

    @teststep
    def click_first_tea(self):
        self.driver.find_element_by_xpath('//*[@resource-id="app"]/android.view.View[6]/android.view.View[1]/android.view.View[4]').click()
        print('点击 第一个老师')
        time.sleep(1)

    @teststep
    def click_second_tea(self):
        self.driver.find_element_by_xpath('//*[@resource-id="app"]/android.view.View[6]/android.view.View[1]/android.view.View[6]').click()
        print('点击 第二个老师')
        time.sleep(1)

    @teststep
    def click_export(self):
        self.driver.find_element_by_xpath('//*[@text="导出"]').click()
        print('点击 导出')
        time.sleep(0.5)

    @teststep
    def get_export_tips(self):
        ele_list = self.driver.find_elements_by_xpath('//android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.view.ViewGroup[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[2]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.webkit.WebView[1]/android.webkit.WebView[1]/android.view.View[1]/android.view.View[8]/android.view.View')
        tips = [i.text for i in ele_list[:3]]
        if '(登录电脑版微信操作体验更佳。)' in str(tips):
            print('✅提示(登录电脑版微信操作体验更佳。)')
        else:
            print('❌error:没有 (登录电脑版微信操作体验更佳。) 的提示，请进行检查')

    @teststep
    def click_compared(self):
        self.driver.find_element_by_xpath('//*[@text="对比"]').click()

    @teststep
    def click_all(self):
        self.driver.find_element_by_xpath('//*[@text="全部"]').click()

    @teststep
    def get_show_tea(self):
        tea_nickname = self.driver.find_element_by_xpath('//android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.view.ViewGroup[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[2]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.webkit.WebView[1]/android.webkit.WebView[1]/android.view.View[1]/android.view.View[6]/android.view.View[1]/android.view.View[1]').text
        print('显示的教师名是：%s'%tea_nickname)
        if tea_nickname == '你好 World':
            print('✅教师切换成功')
        else:
            print('\n\t❌error:教师切换失败，请进行检查\n')

    @teststep
    def click_help(self):
        self.driver.find_element_by_xpath('//*[@text=""]').click()
        print('点击 问号')
        time.sleep(2)

    @teststep
    def click_cancel(self):
        self.driver.find_element_by_xpath('//*[@text="取消"]').click()
        print('点击 取消')
        time.sleep(1)

    @teststep
    def click_ensure(self):
        # self.driver.find_element_by_xpath('//*[@text="确定"]').click()
        click_bounds(self,700,1940)
        print('点击 确定')
        time.sleep(1.5)

    @teststep
    def click_reset(self):
        # self.driver.find_element_by_xpath('//*[@text="重置"]').click()
        click_bounds(self,210,1940)
        print('点击 重置')
        time.sleep(1)

    @teststep
    def last_weak(self,weeks = -1):
        today = datetime.date.today()
        last_monday = (today + datetime.timedelta(days=-today.weekday(),weeks=weeks)).strftime('%m/%d')
        last_sunday = (today + datetime.timedelta(days=-today.weekday() - 1, weeks= weeks + 1)).strftime('%m/%d')
        # print('last_mondy:',last_monday,'\t','last_sunday:',last_sunday)
        return last_monday,last_sunday

    @teststep
    def last_month(self):
        month = int(time.strftime('%m')) - 1
        last_day = calendar.monthrange(2019, month)[-1]
        last_day = '%s/%s' % (str(month).rjust(2, '0'), last_day)
        first_day = '%s/%s' % (str(month).rjust(2, '0'), '01')
        return first_day,last_day

    @teststep
    def get_all_info(self):
        ele_list = self.driver.find_elements_by_xpath('//android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.view.ViewGroup[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[2]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.webkit.WebView[1]/android.webkit.WebView[1]/android.view.View[1]/android.view.View[6]/android.view.View')
        return ele_list