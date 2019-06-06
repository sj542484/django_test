import time
from testfarm.test_program.conf.decorator import teststep, teststeps
from testfarm.test_program.conf.basepage import BasePage

class Login_page(BasePage):
    """登录页面"""

    @teststeps
    def click_more(self):
        """点击更多用于用于切换账号"""
        time.sleep(1)
        self.driver.element_by_id('com.tencent.mm:id/bwu').click()

    @teststeps
    def click_more_account(self):
        time.sleep(1)
        self.driver.element_by_name('登录其他帐号').click()

    @teststeps
    def password(self):
        time.sleep(1)
        ele = self.driver.element_by_name('密码').text
        return ele