import time
# from macaca import WebDriverException
from testfarm.test_program.conf.decorator import teststep, teststeps
from testfarm.test_program.conf.basepage import BasePage
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
import re

class HomePage(BasePage):
    """主界面"""
    @teststeps
    def my_self_text(self):
        """点击我进入微信的个人界面 """
        time.sleep(1)
        ele = self.driver.element_by_name('我').text
        return ele

    @teststeps
    def click_contacts(self):
        """点击通讯录进入通讯录列表"""
        time.sleep(1)
        self.driver.find_element_by_xpath('//*[@text="通讯录"]').click()
        print("点击通讯录")

    @teststeps
    def click_public(self):
        """点击公众号进入公众号列表"""
        time.sleep(1)
        self.driver.find_element_by_xpath('//*[@resource-id="com.tencent.mm:id/a5t"]').click()
        print("点击公众号，进入公众号")

    @teststeps
    def click_start(self):
        """点击万星在线进入万兴公众号"""
        time.sleep(2)
        self.driver.find_element_by_xpath('//*[@text="万星在线"]').click()

    @teststeps
    def account_management(self):
        """点击账户管理"""
        time.sleep(1)
        self.driver.find_element_by_xpath('//*[@text="账户管理"]').click()
        print("点击账户管理")

    @teststeps
    def click_my_school(self):
        """点击我的学校"""
        time.sleep(2)
        self.driver.find_element_by_xpath('//*[@text="我的学校"]').click()
        print("进入我的学校")

    @teststeps
    def click_my_account(self):
        """点击我的账号"""
        time.sleep(2)
        self.driver.find_element_by_xpath('//*[@text="我的账号"]').click()
        print("进入我的账号")

    @teststep
    def click_teacher_manage(self):
        time.sleep(2)
        self.driver.find_element_by_xpath('//*[@text="老师管理"]').click()
        print('点击 老师管理')

    @teststeps
    def click_data_report(self):
        self.driver.find_element_by_xpath('//*[@text="数据报告"]').click()
        print('点击 数据报告')
        time.sleep(1.5)

    @teststeps
    def click_homework_statistics(self):
        self.driver.find_element_by_xpath('//*[@text="作业统计"]').click()
        print('点击 作业统计')
        time.sleep(1)

    @teststeps
    def wait_homeword_statistics(self):
        try:
            ele = (By.XPATH, '//*[@text="上上周"]')
            WebDriverWait(self.driver, 15, 0.5).until(EC.presence_of_element_located(ele))
            return True
        except:
            return False

    @teststeps
    def wait_integral_statistics(self):
        try:
            ele = (By.XPATH, '//*[@text="上上周"]')
            WebDriverWait(self.driver, 15, 0.5).until(EC.presence_of_element_located(ele))
            return True
        except:
            return False

    @teststeps
    def click_integral_statistics(self):
        self.driver.find_element_by_xpath('//*[@text="积分统计"]').click()
        print('点击 积分统计')
        time.sleep(1)

    @teststeps
    def wait_check_parent_title(self):
        try:
            ele = (By.XPATH, "//android.widget.TextView[contains(@text,'在线助教家长')]")
            WebDriverWait(self.driver,15, 0.5).until(EC.presence_of_element_located(ele))
            return True
        except:
            return False

    @teststeps
    def wait_check_findText(self):
        try:
            ele = (By.XPATH, "//android.widget.TextView[contains(@text,'搜索指定内容')]")
            WebDriverWait(self.driver, 15, 0.5).until(EC.presence_of_element_located(ele))
            return True
        except:
            return False

    @teststeps
    def click_find_icon(self):
        self.driver.find_element_by_accessibility_id("搜索").click()
        time.sleep(2)

    @teststeps
    def wait_check_login_page(self):
        """以title：“登录”的text为依据"""
        try:
            locator = (By.XPATH, "//android.widget.TextView[contains(@text,'登录')]")
            WebDriverWait(self.driver, 15, 0.5).until(EC.presence_of_element_located(locator))
            return True
        except:
            return False

    @teststep
    def login_phone(self):
        """手机号 输入框的text为依据"""
        ele = self.driver.find_element_by_accessibility_id("请输入手机号")
        return ele

    @teststep
    def login_password(self):
        """密码 输入框的text为依据"""
        ele = self.driver.find_element_by_xpath("//android.webkit.WebView[1]/android.webkit.WebView[1]/android.view.View[5]/android.widget.EditText[1]")
        return ele

    @teststep
    def login_button(self):
        """登录 button的text为依据"""
        self.driver.find_element_by_class_name("android.widget.Button").click()