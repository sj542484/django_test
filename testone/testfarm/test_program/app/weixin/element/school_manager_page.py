import re
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from testfarm.test_program.conf.decorator import teststep
from testfarm.test_program.conf.basepage import BasePage


class SchoolManagerPage(BasePage):
    @teststep
    def wait_school_manager_page(self):
        try:
            ele = (By.XPATH, '//*[@text="小玉5.21测试"]')
            WebDriverWait(self.driver, 10, 0.3).until(EC.presence_of_element_located(ele))
            return True
        except:
            return False

    @teststep
    def wait_success_page(self):
        try:
            ele = (By.XPATH, '//*[@text="提交成功!"]')
            WebDriverWait(self.driver, 5, 0.3).until(EC.presence_of_element_located(ele))
            return True
        except:
            return False

    @teststep
    def wait_privew_page(self):
        try:
            ele = (By.XPATH, '//android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.view.ViewGroup[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[2]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.webkit.WebView[1]/android.webkit.WebView[1]/android.view.View[1]/android.view.View[3]/android.widget.Button[1]')
            WebDriverWait(self.driver, 5, 0.3).until(EC.presence_of_element_located(ele))
            return True
        except:
            return False

    @teststep
    def click_sch_manager(self):
        self.driver.find_element_by_xpath(
            '//android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.view.ViewGroup[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[2]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.webkit.WebView[1]/android.webkit.WebView[1]/android.view.View[1]/android.view.View[2]/android.view.View[5]/android.view.View[7]'
        ).click()
        time.sleep(0.5)

    @teststep
    def get_tips(self):
        info = self.driver.find_element_by_xpath('//android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.view.ViewGroup[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[2]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.webkit.WebView[1]/android.webkit.WebView[1]/android.view.View[2]').text
        return info

    @teststep
    def get_tips_in_page(self):
        info = self.driver.find_element_by_xpath('//android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.view.ViewGroup[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[2]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.webkit.WebView[1]/android.webkit.WebView[1]/android.view.View[1]/android.view.View[3]/android.view.View[1]/android.view.View[2]').text
        info_tips = self.driver.find_element_by_xpath('//android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.view.ViewGroup[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[2]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.webkit.WebView[1]/android.webkit.WebView[1]/android.view.View[1]/android.view.View[3]/android.view.View[1]/android.view.View[4]').text
        if info == '批量输入（校管帐号，不是老师帐号，请注意）':
            if info_tips == '【姓名 + 空格 + 手机号】如：王某某 15200000000 ；一行一人，输入完成后，点击【预览】，检查所输入内容':
                print('✅页面提示词正常')
            else:
                print('❌error:学校管理-批量输入页面提示词异常，请进行检查',info_tips)
        else:
            print('❌error:学校管理-批量输入页面提示词异常，请进行检查', info)

    @teststep
    def click_creat_school_manager(self):
        self.driver.find_element_by_xpath('//*[@text="新建学校管理员"]').click()
        time.sleep(1)

    @teststep
    def click_creat_manager(self):
        self.driver.find_element_by_xpath('//android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.view.ViewGroup[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[2]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.webkit.WebView[1]/android.webkit.WebView[1]/android.view.View[1]/android.view.View[4]/android.widget.Button[1]').click()
        time.sleep(1)

    @teststep
    def input_info(self,school_manager_info):
        self.driver.find_element_by_xpath(\
            '//android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.view.ViewGroup[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[2]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.webkit.WebView[1]/android.webkit.WebView[1]/android.view.View[1]/android.view.View[3]/android.view.View[1]/android.view.View[3]/android.view.View[2]/android.widget.EditText[1]'\
                                          ).send_keys(school_manager_info)

    @teststep
    def click_preview(self):
        self.driver.find_element_by_xpath('//android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.view.ViewGroup[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[2]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.webkit.WebView[1]/android.webkit.WebView[1]/android.view.View[1]/android.view.View[3]/android.widget.Button[1]').click()
        time.sleep(1)

    @teststep
    def click_warning_first(self):
        self.driver.find_element_by_xpath('//*[@resource-id="app"]/android.view.View[3]/android.view.View[2]/android.view.View[2]/android.view.View[3]/android.view.View[1]/android.view.View[1]').click()
        time.sleep(0.3)

    @teststep
    def click_warning_second(self):
        self.driver.find_element_by_xpath('//*[@resource-id="app"]/android.view.View[3]/android.view.View[2]/android.view.View[3]/android.view.View[4]/android.view.View[1]/android.view.View[1]').click()
        time.sleep(0.3)

    @teststep
    def modify_info_name(self):
        self.driver.find_element_by_xpath('//android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.view.ViewGroup[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[2]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.webkit.WebView[1]/android.webkit.WebView[1]/android.view.View[1]/android.view.View[3]/android.view.View[2]/android.view.View[2]/android.view.View[2]/android.widget.EditText[1]').send_keys('猪猪侠')

    @teststep
    def modify_info_phone(self):
        self.driver.find_element_by_xpath('//*[@resource-id="app"]/android.view.View[3]/android.view.View[2]/android.view.View[3]/android.view.View[3]/android.widget.EditText[1]').send_keys('13233333331')

    @teststep
    def modify_info_last_phone(self):
        self.driver.find_element_by_xpath('//android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.view.ViewGroup[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[2]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.webkit.WebView[1]/android.webkit.WebView[1]/android.view.View[1]/android.view.View[3]/android.view.View[4]/android.view.View[3]/android.view.View[3]/android.widget.EditText[1]').send_keys('13444442222')

    @teststep
    def get_success_info(self):
        info_ele = self.driver.find_elements_by_xpath('//android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.view.ViewGroup[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[2]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.webkit.WebView[1]/android.webkit.WebView[1]/android.view.View[1]/android.view.View[3]/android.view.View')
        info_list = [i.text for i in info_ele[2:]]
        print(info_list)
        return info_list

    @teststep
    def get_school_manager_num(self):
        info = self.driver.find_element_by_xpath('//android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.view.ViewGroup[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[2]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.webkit.WebView[1]/android.webkit.WebView[1]/android.view.View[1]/android.view.View[3]/android.view.View[1]/android.view.View[1]').text
        num = re.findall('\d+',info)[0]
        return int(num)

    @teststep
    def get_school_manager_info(self):
        page_info = self.driver.page_source
        pat = re.compile(r'text="([\u4e00-\u9fa50-9 ]+)"')
        page_info = pat.findall(page_info)
        print('添加的校管信息：',page_info)
        ele = self.driver.find_elements_by_xpath('//android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.view.ViewGroup[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[2]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.webkit.WebView[1]/android.webkit.WebView[1]/android.view.View[1]/android.view.View[3]/android.view.View[1]/android.view.View[2]/android.view.View')
        return ele[1:-1],page_info

    @teststep
    def click_frozen(self):
        self.driver.find_element_by_xpath('//*[@resource-id="app"]/android.view.View[3]/android.view.View[3]/android.view.View[2]/android.view.View[2]').click()
        time.sleep(0.5)

    @teststep
    def click_unbind(self):
        self.driver.find_element_by_xpath('//*[@resource-id="app"]/android.view.View[3]/android.view.View[5]').click()
        time.sleep(1)

    @teststep
    def click_first_manager(self):
        self.driver.find_element_by_xpath('//android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.view.ViewGroup[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[2]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.webkit.WebView[1]/android.webkit.WebView[1]/android.view.View[1]/android.view.View[3]/android.view.View[1]/android.view.View[2]/android.view.View[2]').click()
        time.sleep(1)