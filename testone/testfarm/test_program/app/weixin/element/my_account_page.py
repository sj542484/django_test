import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from testfarm.test_program.app.weixin.test_data.school_name import schoolInfo
from testfarm.test_program.conf.decorator import teststep
from testfarm.test_program.conf.basepage import BasePage

class MyAccountPage(BasePage):
    @teststep
    def wait_my_account_page(self):
        locator = (By.XPATH, '//*[@text="我的账号"]')
        try:
            WebDriverWait(self.driver, 10, 0.3).until(lambda x: x.find_element(*locator))
            return True
        except:
            return False

    @teststep
    def wait_set_pwd_page(self):
        locator = (By.XPATH, '//*[@text="设置密码"]')
        try:
            WebDriverWait(self.driver, 10, 0.3).until(lambda x: x.find_element(*locator))
            return True
        except:
            return False

    @teststep
    def wait_bind_page(self):
        locator = (By.XPATH, '//*[@text="绑定手机号"]')
        try:
            WebDriverWait(self.driver, 15, 0.3).until(lambda x: x.find_element(*locator))
            return True
        except:
            return False

    @teststep
    def get_info(self):
        name = self.name_ele().text
        phone_number = self.phone_ele().text
        wechat = self.wechat_ele().text
        pwd = self.pwd_ele().text
        identity = self.identity_ele().text
        print('name:',name,'phone_number:',phone_number,'wechat:',wechat,'pwd:',pwd,'identity:',identity)
        return name,phone_number,wechat,pwd,identity

    @teststep
    def name_ele(self):
        ele = self.driver.find_element_by_xpath(
            '//android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.view.ViewGroup[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[2]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.webkit.WebView[1]/android.webkit.WebView[1]/android.view.View[1]/android.view.View[2]/android.view.View[1]/android.view.View[2]/android.view.View[2]/android.view.View[1]')
        return ele

    @teststep
    def click_name(self):
        self.name_ele().click()
        time.sleep(1)

    @teststep
    def input_name(self):
        minute_now = time.strftime('%M')
        self.driver.find_element_by_xpath(
            '//*[@resource-id="app"]/android.view.View[4]/android.view.View[2]/android.widget.EditText[1]').send_keys(
            '时晓专用%s' % minute_now)
        return '时晓专用%s'%minute_now

    @teststep
    def phone_ele(self):
        ele = self.driver.find_element_by_xpath(
            '//android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.view.ViewGroup[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[2]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.webkit.WebView[1]/android.webkit.WebView[1]/android.view.View[1]/android.view.View[2]/android.view.View[1]/android.view.View[3]')
        return ele

    @teststep
    def click_phone(self):
        self.pwd_ele().click()
        time.sleep(1)

    @teststep
    def wechat_ele(self):
        ele = self.driver.find_element_by_xpath(
            '//android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.view.ViewGroup[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[2]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.webkit.WebView[1]/android.webkit.WebView[1]/android.view.View[1]/android.view.View[2]/android.view.View[1]/android.view.View[4]/android.view.View[3]/android.view.View[1]')
        return ele

    @teststep
    def pwd_ele(self):
        ele = self.driver.find_element_by_xpath(
            '//android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.view.ViewGroup[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[2]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.webkit.WebView[1]/android.webkit.WebView[1]/android.view.View[1]/android.view.View[2]/android.view.View[1]/android.view.View[5]')
        return ele

    @teststep
    def identity_ele(self):
        ele = self.driver.find_element_by_xpath(
            '//android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.view.ViewGroup[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[2]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.webkit.WebView[1]/android.webkit.WebView[1]/android.view.View[1]/android.view.View[2]/android.view.View[1]/android.view.View[6]/android.view.View[3]/android.view.View[1]')
        return ele

    @teststep
    def click_cancel(self):
        self.driver.find_element_by_xpath(
            '//android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.view.ViewGroup[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[2]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.webkit.WebView[1]/android.webkit.WebView[1]/android.view.View[1]/android.view.View[4]/android.view.View[3]/android.view.View[1]'
        ).click()
        print('点击 取消')
        time.sleep(0.3)

    @teststep
    def click_ensure(self):
        self.driver.find_element_by_xpath(
            '//android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.view.ViewGroup[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[2]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.webkit.WebView[1]/android.webkit.WebView[1]/android.view.View[1]/android.view.View[4]/android.view.View[3]/android.view.View[2]'
        ).click()
        print('点击 确定')
        time.sleep(0.3)

    @teststep
    def click_quit(self):
        self.driver.find_element_by_xpath(
            '//*[@resource-id="app"]/android.view.View[2]/android.widget.Button'
            # '//android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.view.ViewGroup[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[2]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.webkit.WebView[1]/android.webkit.WebView[1]/android.view.View[1]/android.view.View[2]/android.widget.Button[1]'
        ).click()
        print('点击 退出登陆')
        time.sleep(0.3)

    @teststep
    def click_quit_ensure(self):
        self.driver.find_element_by_xpath(
            '//*[@text="确定"]'
            # '//android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.view.ViewGroup[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[2]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.webkit.WebView[1]/android.webkit.WebView[1]/android.view.View[2]/android.view.View[2]/android.view.View[2]/android.view.View[2]'
        ).click()
        print('点击 退出确认')
        time.sleep(1)

    @teststep
    def click_quit_cancel(self):
        self.driver.find_element_by_xpath(
            '//*[@text="取消"]'
            # '//android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.view.ViewGroup[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[2]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.webkit.WebView[1]/android.webkit.WebView[1]/android.view.View[2]/android.view.View[2]/android.view.View[2]/android.view.View[1]'
        ).click()
        print('点击 退出取消')
        time.sleep(0.5)

    @teststep
    def input_username(self,phone_number):
        self.driver.find_element_by_xpath(
            '//*[@text="请输入手机号"]'
        ).send_keys(phone_number)
        return phone_number

    @teststep
    def click_get_verification(self):
        self.driver.find_element_by_xpath(
            '//*[@text="获取验证码"]'
        ).click()

    @teststep
    def input_verification(self,verification):
        self.driver.find_element_by_xpath(
            '//*[@text="请输入验证码"]'
        ).send_keys(verification)
        time.sleep(1)

    @teststep
    def click_bind_login(self):
        self.driver.find_element_by_xpath(
            '//*[@text="绑定手机号"]/following-sibling::android.widget.Button[1]'
        ).click()
        time.sleep(1)

    @teststep
    def click_bind_success_ensure(self):
        self.driver.find_element_by_xpath(
          '//*[@text="确定"]'
        ).click()
        time.sleep(0.5)

    @teststep
    def click_apply(self):
        self.driver.find_element_by_xpath(
            '//android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.view.ViewGroup[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[2]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.webkit.WebView[1]/android.webkit.WebView[1]/android.view.View[1]/android.view.View[3]/android.view.View[2]'
        ).click()
        time.sleep(0.5)

    @teststep
    def click_bind_now(self):
        self.driver.find_element_by_xpath(
            '//android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.view.ViewGroup[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[2]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.webkit.WebView[1]/android.webkit.WebView[1]/android.view.View[1]/android.view.View[3]/android.view.View[2]'
        ).click()
        time.sleep(0.5)

    @teststep
    def apply_sch_name(self,sch_name):
        self.driver.find_element_by_xpath(
            '//android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.view.ViewGroup[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[2]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.webkit.WebView[1]/android.webkit.WebView[1]/android.view.View[1]/android.view.View[1]/android.view.View[3]/android.view.View[3]/android.widget.EditText[1]'
        ).send_keys(sch_name)

    @teststep
    def apply_sch_nickname(self,sch_nickname):
        self.driver.find_element_by_xpath(
            '//android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.view.ViewGroup[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[2]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.webkit.WebView[1]/android.webkit.WebView[1]/android.view.View[1]/android.view.View[1]/android.view.View[4]/android.view.View[3]/android.widget.EditText[1]'
        ).send_keys(sch_nickname)

    @teststep
    def apply_principal_name(self,principal_name):
        self.driver.find_element_by_xpath(
            '//android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.view.ViewGroup[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[2]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.webkit.WebView[1]/android.webkit.WebView[1]/android.view.View[1]/android.view.View[1]/android.view.View[7]/android.view.View[3]/android.widget.EditText[1]'
        ).send_keys(principal_name)

    @teststep
    def apply_wechat(self,wechat):
        self.driver.find_element_by_xpath(
            '//android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.view.ViewGroup[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[2]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.webkit.WebView[1]/android.webkit.WebView[1]/android.view.View[1]/android.view.View[1]/android.view.View[8]/android.view.View[3]/android.widget.EditText[1]'
        ).send_keys(wechat)

    @teststep
    def apply_principal_phone(self, principal_phone):
        self.driver.find_element_by_xpath(
            '//android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.view.ViewGroup[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[2]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.webkit.WebView[1]/android.webkit.WebView[1]/android.view.View[1]/android.view.View[1]/android.view.View[10]/android.view.View[3]/android.widget.EditText[1]'
     ).send_keys(principal_phone)

    @teststep
    def input_all_info(self):
        self.apply_sch_name(schoolInfo['schoolName'])
        time.sleep(0.5)
        self.apply_sch_nickname(schoolInfo['schoolNickname'])
        time.sleep(0.5)
        self.apply_principal_name(schoolInfo['principalName'])
        time.sleep(0.5)
        self.apply_principal_phone(schoolInfo['principalPhone'])
        time.sleep(0.5)
        self.apply_wechat(schoolInfo['wechat'])
        time.sleep(1)
        return schoolInfo['principalPhone']

    @teststep
    def apply_click_get_verification(self):
        self.driver.find_element_by_xpath(
            '//android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.view.ViewGroup[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[2]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.webkit.WebView[1]/android.webkit.WebView[1]/android.view.View[1]/android.view.View[1]/android.view.View[11]/android.view.View[4]/android.view.View[1]'
        ).click()

    @teststep
    def apply_input_verification(self,verification):
        self.driver.find_element_by_xpath(
            '//android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.view.ViewGroup[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[2]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.webkit.WebView[1]/android.webkit.WebView[1]/android.view.View[1]/android.view.View[1]/android.view.View[11]/android.view.View[3]/android.widget.EditText[1]'
        ).send_keys(verification)

    @teststep
    def apply_click_apply(self):
        self.driver.find_element_by_xpath(
            '//android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.view.ViewGroup[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[2]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.webkit.WebView[1]/android.webkit.WebView[1]/android.view.View[1]/android.view.View[2]'
        ).click()
        time.sleep(1)

    @teststep
    def click_location(self):
        self.driver.find_element_by_xpath(
            '//android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.view.ViewGroup[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[2]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.webkit.WebView[1]/android.webkit.WebView[1]/android.view.View[1]/android.view.View[1]/android.view.View[5]/android.view.View[3]'
        ).click()
    time.sleep(2.5)

    @teststep
    def input_pwd(self):
        self.driver.find_element_by_xpath('//*[@text="请输入密码"]').send_keys('123321')
        time.sleep(0.5)

    @teststep
    def input_pwd_again(self):
        self.driver.find_element_by_xpath('//*[@text="请再次输入密码"]').send_keys('123321')
        time.sleep(0.5)

    @teststep
    def click_set_pwd(self):
        self.driver.find_element_by_xpath('//*[@text="设置密码"]').click()
        time.sleep(1)

    @teststep
    def click_ensure_in_last(self):
        self.driver.find_element_by_xpath(
          '//*[@text="密码由6-20位英文字母或数字组成"]/following-sibling::android.widget.Button'
        ).click()
        time.sleep(2)