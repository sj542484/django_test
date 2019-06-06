import time
import os
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from testfarm.test_program.app.weixin.element.main_page import HomePage
from testfarm.test_program.conf.decorator import teststep, teststeps
from testfarm.test_program.conf.basepage import BasePage
from selenium.webdriver.common.by import By
from testfarm.test_program.utils.toast_find import Toast


class Loginpage(BasePage):
    """登录界面"""

    @teststeps
    def __init__(self):
        self.home = HomePage()
        self.toast = Toast()
    @teststeps

    def wait_check_wx(self):
        """以微信主界面“tab:微信”的text为依据"""
        try:
            main_ele = (By.XPATH, "//android.widget.TextView[contains(@text,'微信')]")
            WebDriverWait(self.driver, 15, 0.5).until(EC.presence_of_element_located(main_ele))
            return True
        except :
            return False

    @teststep
    def launch_app(self):
        """Start on the device the application specified in the desired capabilities.
        """
        os.system ("adb shell am start -n com.tencent.mm/com.tencent.mm.ui.LauncherUI/")
        time.sleep (5)

    @teststep
    def close_app(self):
        """Close on the device the application specified in the desired capabilities.
        """
        os.system ('adb shell am force-stop com.tencent.mm')

    @teststeps
    def app_status(self):
        """判断应用当前状态"""

        if self.wait_check_wx():  # 在 微信 界面
            print('微信主界面：')
            self.clear_tbs()
        elif self.home.wait_check_parent_title():  # 家长端 主界面

            print('家长端 主界面：')
        else:
            print('其他情况：')
            self.close_app()
            self.launch_app()
            if self.wait_check_wx():  # 在 微信 主界面
                print('微信主界面：')

    @teststep
    def chat_test1_click(self):
        """点击置顶好友test1"""
        self.driver.element_by_xpath('//*[@resource-id="com.tencent.mm:id/auj"]').click()
    @teststep
    def chat_test1_click_my(self):
        """点击置顶好友test1"""
        self.driver.find_element_by_xpath('//XCUIElementTypeStaticText[@name="夜雨声烦。"]').click()

    @teststep
    def tbs_link_click(self):
        """点击test1发送的tbs链接"""
        self.driver.find_element_by_xpath('//XCUIElementTypeOther[@name="夜雨声烦。说debugtbs.qq.com"]').click()
        print("点击链接结束")

    @teststep
    def click_clear_tbs_btn(self):
        """点击清除tbs内核选项"""
        self.driver.element_by_xpath ('//*[@text="清除TBS内核"]').click()

    @teststep
    def confirm_delete(self):
        """确认清除"""
        time.sleep(5)
        self.driver.element_by_id ("android:id/button1").click()
        time.sleep (2)

    @teststep
    def back_to_test1(self):
        """点击返回按钮（X） 返回到聊天框"""
        time.sleep(5)
        self.driver.element_by_id ("com.tencent.mm:id/j7").click()

    @teststep
    def back_to_wx_home(self):
        time.sleep(5)
        self.driver.touch("tap", {"x": 44, "y": 99})

    @teststep
    def clear_tbs(self):
        """进入清除内核页面，并返回主页面"""
        self.chat_test1_click_my()
        # if self.wait_check_test1():
        time.sleep(5)
        self.tbs_link_click()      #点击链接
        time.sleep(5)
        self.click_clear_tbs_btn()  #点击清除tbs
        time.sleep(2)
         # if self.wait_check_delete_x5core():
        self.confirm_delete()   #确认清除
        time.sleep(2)
        self.back_to_test1()   # 退出tbs页面
        # if self.wait_check_test1():
        self.back_to_wx_home() #退出聊天页面
        time.sleep(5)
                        # if self.wait_check_wx():
        print("已清除TBS内核\n")
