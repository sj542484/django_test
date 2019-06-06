import time
from testfarm.test_program.app.student.login.test_data.account import VALID_ACCOUNT,VALID_ACCOUNT1
from testfarm.test_program.app.weixin.element.main_page import HomePage
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from testfarm.test_program.conf.decorator import teststep
from testfarm.test_program.conf.basepage import BasePage
from testfarm.test_program.app.weixin.element.login_page import Login_page
import os


class LoginPage(BasePage):

    @teststep
    def input_username(self, username):
        """以“请输入手机号码”的TEXT为依据"""
        self.driver.element_by_id('com.tencent.mm:id/hx').send_keys(username)

    @teststep
    def click_next(self):
        # 点击下一步
        time.sleep(2)
        self.driver.element_by_name("下一步").click()

    @teststep
    def wait_check_page_index(self):
        """以“title:重置密码”的xpath @text为依据"""
        locator = (By.XPATH, '//*[@text="我"]')
        try:
            WebDriverWait(self.driver, 20, 0.5).until(lambda x: x.find_element(*locator))
            return True
        except:
            return False

    @teststep
    def input_password(self, password):
        """以“请输入登录密码”的XPATH为依据"""
        # 输入密码
        self.driver.element_by_xpath('//*[@resource-id="com.tencent.mm:id/cb_"]/android.widget.EditText[1]').send_keys(password)

    @teststep
    def login_button(self):
        """以“登录”Button的ID为依据"""
        # 点击登录
        self.driver.element_by_name('登录').click()

    @teststep
    def register(self):
         # 以“注册帐号”的ID为依据"

        self.driver.find_element_by_xpath('//XCUIElementTypeButton[@name="注 册"]').click()
    #
    @teststep
    def remember_password(self):
    #     """以“显示密码”的ID为依据"""
         self.driver.find_element_by_xpath('//XCUIElementTypeButton[@name="btn ic eye off"]').click()
    #
    #
    @teststep
    def forget_password(self):
    # 以“忘记密码？”的ID为依据

         self.driver.find_element_by_xpath('//XCUIElementTypeButton[@name="忘记密码"]').click()

    @teststep
    def login(self):
        """用给定的account与password进行登录"""
        # 等待login页面activity出现
        # self.driver.wait_activity("com.vanthink.vanthinkstudent.v2.ui.user.login.LoginActivity", 10)
        time.sleep(10)

        self.input_username(VALID_ACCOUNT.account())
        self.input_password(VALID_ACCOUNT.password())
        self.login_button()
        time.sleep(10)

    @teststep
    def login1(self):
        """用给定的account与password进行登录"""
        # 等待login页面activity出现
        # self.driver.wait_activity("com.vanthink.vanthinkstudent.v2.ui.user.login.LoginActivity", 10)
        time.sleep(10)

        self.input_username(VALID_ACCOUNT1.account1())
        self.input_password(VALID_ACCOUNT1.password1())
        self.login_button()
        time.sleep(10)

    @teststep
    def weixin_login(self):
        """用给定的account与password进行登录"""
        # 等待login页面activity出现
        # self.driver.wait_activity("com.vanthink.vanthinkstudent.v2.ui.user.login.LoginActivity", 10)
        time.sleep(3)
        self.input_username(VALID_ACCOUNT.account())
        self.click_next()
        self.input_password(VALID_ACCOUNT.password())
        self.login_button()
        time.sleep(3)




    def wait_check_page(self):
        """以“title:登录”的class_name为依据"""
        try:
            ele = (By.XPATH, '//XCUIElementTypeButton[@name="忘记密码"]')
            WebDriverWait(self.driver, 5, 0.3).until(EC.presence_of_element_located(ele))
            return True
        except:
            return False

    @teststep
    def app_status(self):
        """判断应用当前状态"""
        time.sleep(3)
        source = self.driver.page_source
        if '忘记密码' in source:

            self.login()

        elif '试卷' in source:
            print('登录成功')
        else:
            self.close_app()
            self.launch_app()
            if self.wait_check_page():
                self.login()
            else:
                print('已登录')
    @teststep
    def app_status1(self):
        """判断应用当前状态"""
        time.sleep(3)
        source = self.driver.page_source
        if '忘记密码' in source:

            self.login1()

        elif '试卷' in source:
            print('登录成功')
        else:
            self.close_app()
            self.launch_app()
            if self.wait_check_page():
                self.login1()
            else:
                print('已登录')

    @teststep
    def wait_check_main_page(self):
        ''''''
        try:
            ele = (By.XPATH, '//*[@text="我"]')
            WebDriverWait(self.driver, 5, 0.3).until(EC.presence_of_element_located(ele))
            return True
        except:
            return False

    @teststep
    def weixin_app_status(self):
        """判断应用当前状态"""
        time.sleep(2)
        if '我' == HomePage().my_self_text():
            print('登录成功')

        elif '密码' == Login_page().password():
            print("进入判断")
            Login_page().click_more()
            Login_page().click_more_account()
            self.weixin_login()
        else:
            self.close_app_operate()
            self.launch_app_operate()
            if self.wait_check_page():
                self.login()
            else:
                print('已登录')
    @teststep
    def weixin_app(self):
        """判断应用当前状态"""
        time.sleep(3)
        if self.wait_check_main_page():
            print('登录成功')
            time.sleep(2)
        else:
            self.close_app_weixin()
            self.launch_app_weixin()
            if self.wait_check_page():
                self.login()
            else:
                print('已登录')


    def click_weixin(self):
        # 点击微信回到主页面
        self.driver.find_element_by_xpath('//*[@text="微信"]').click()

    def click_avatar(self):
        time.sleep(3)
        self.driver.find_element_by_xpath('//*[@text="停用"]').click()
        print('点击微信头像～～内核清理')

    def click_link_wait(self):
        locator = (By.XPATH, '//android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[2]/android.widget.FrameLayout[1]/android.widget.ListView[1]/android.widget.RelativeLayout[1]/android.widget.LinearLayout[1]/android.widget.LinearLayout[1]')
        try:
            WebDriverWait(self.driver, 20, 0.5).until(lambda x: x.find_element(*locator))
            return True
        except:
            return False

    def click_link(self):
        # 点击连接
        self.driver.find_element_by_xpath('//*[@resource-id="com.tencent.mm:id/aa"]/android.widget.LinearLayout[1]').click()
        time.sleep(1.5)
        print('点击连接')

    def judgment_page(self):
        # 判断是否进入tbs调试界面
        locator = (By.XPATH, '//*[@text="清除TBS内核"]')
        try:
            WebDriverWait(self.driver, 20, 0.5).until(lambda x: x.find_element(*locator))
            return True
        except:
            return False

    def click_clear_kernel(self):
        # 点击清除tbs内核
        self.driver.find_element_by_xpath('//*[@text="清除TBS内核"]').click()
        print("点击清除tbs内核")

    def click_determine(self):
        # 点击确定
        time.sleep(1.5)
        self.driver.find_element_by_xpath('//*[@resource-id="android:id/button1"]').click()
        print("清除tbs内核成功")

    def click_cross(self):
        # 点击叉退出tps调试页面
        time.sleep(1.5)
        self.driver.find_element_by_xpath('//*[@resource-id="com.tencent.mm:id/kb"]').click()

    def click_btn(self):
        # 点击返回
        time.sleep(1)
        self.driver.find_element_by_xpath('//*[@resource-id="com.tencent.mm:id/k1"]').click()
        print("回到微信主界面开始执行应用脚本")
        time.sleep(1)


    @teststep
    def launch_app(self):
        """Start on the device the application specified in the desired capabilities.
        """
        self.driver.launch_app()
        time.sleep(5)

    @teststep
    def close_app(self):
        """Close on the device the application specified in the desired capabilities.
        """
        self.driver.close_app()

    @teststep
    def remove_app(self):
        """Remove on the device the application
        """
        self.driver.remove_app("com.vanthink.student.debug")

    @teststep
    def is_app_installed(self):
        """Check app was installed on the device the application
        """
        self.driver.is_app_installed("com.vanthink.student.debug")

    @teststep
    def launch_app_operate(self):
        """Start on the device the application specified in the desired capabilities.
        """
        self.driver.launch_app(gv.APP)
        time.sleep(5)

    @teststep
    def close_app_operate(self):
        """Close on the device the application specified in the desired capabilities.
        """
        os.system('adb shell am force - stop com.tencent.mm')

    @teststep
    def remove_app(self):
        """Remove on the device the application
        """
        self.driver.remove_app(gv.APP)

    @teststep
    def is_app_installed_operate(self):
        """Check app was installed on the device the application
        """
        self.driver.is_app_installed(gv.APP)

    @teststep
    def install_app_operate(self):
        """Remove on the device the application
        """
        self.driver.install_app(gv.APP)
        print('安装APP')

    @teststep
    def quit(self):
        self.driver.quit()

    @teststep
    def launch_app_weixin(self):
        """Start on the device the application specified in the desired capabilities.
        """
        os.system("adb shell am start -n com.tencent.mm/com.tencent.mm.ui.LauncherUI")
        time.sleep(5)

    @teststep
    def close_app_weixin(self):
        """Close on the device the application specified in the desired capabilities.
        """
        os.system('adb shell am force-stop com.tencent.mm')

    def clear_kernel(self):
        # 清理微信的内核
        # 点击微信头像
        self.click_avatar()
        print('点击 进入 停用')
        # 点击头像中的连接
        if self.click_link_wait():
            self.click_link()
            print('点击 连接～清理内核')
            # 判断是否进入tbs调试页面
            if self.judgment_page():
                # 点击清除tbs内核
                self.click_clear_kernel()
        # 点击确定确认清除
        self.click_determine()
        # 点击x退出tbs调试页面
        self.click_cross()
        # 点击返回回到主要页面
        self.click_btn()
