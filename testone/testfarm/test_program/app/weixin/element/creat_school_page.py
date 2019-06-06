import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from testfarm.test_program.conf.decorator import teststep, teststeps
from testfarm.test_program.conf.basepage import BasePage
from testfarm.test_program.utils.click_bounds import click_bounds
from testfarm.test_program.app.weixin.test_data.school_name import schoolName,schoolNickname

class CreatSchoolPage(BasePage):
    @teststeps
    def wait_creat_school_page(self):
        '''新建学校'''
        try:
            ele = (By.XPATH,'//*[@resource-id="app"]/android.view.View[2]')
            WebDriverWait(self.driver, 3, 0.3).until(EC.presence_of_element_located(ele))
            return True
        except:
            return False

    @teststeps
    def wait_school_page(self):
        '''新建学校'''
        try:
            ele = (By.XPATH, '//*[@text="我的学校"]')
            WebDriverWait(self.driver, 3, 0.3).until(EC.presence_of_element_located(ele))
            return True
        except:
            return False

    @teststep
    def slip_up(self):
        time.sleep(1)
        self.driver.swipe(500,1900,500,440,1300)
        print('滑动至底部')
        time.sleep(0.5)

    @teststep
    def click_creat_school(self):
        # self.driver.find_element_by_xpath('//*[@text="创建新学校"]').click()
        click_bounds(self,500,1825)
        print('点击 创建新学校')
        time.sleep(1)

    @teststep
    def input_school_name(self,schoolName):
        self.driver.find_element_by_xpath(
            '//android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.view.ViewGroup[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[2]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.webkit.WebView[1]/android.webkit.WebView[1]/android.view.View[1]/android.view.View[3]/android.view.View[1]/android.view.View[2]/android.view.View[2]/android.widget.EditText[1]').send_keys(schoolName)
        print('输入学校名称')

    @teststep
    def input_nickname(self,nickName):
        self.driver.find_element_by_xpath(
            '//android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.view.ViewGroup[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[2]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.webkit.WebView[1]/android.webkit.WebView[1]/android.view.View[1]/android.view.View[3]/android.view.View[1]/android.view.View[3]/android.view.View[3]/android.widget.EditText[1]').send_keys(nickName)
        print('输入学校简称')

    @teststep
    def get_school_name(self):
        text = self.driver.find_element_by_xpath('//android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.view.ViewGroup[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[2]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.webkit.WebView[1]/android.webkit.WebView[1]/android.view.View[1]/android.view.View[3]/android.view.View[1]/android.view.View[3]/android.view.View[2]').text
        return text

    @teststep
    def get_school_nickname(self):
        text = self.driver.find_element_by_xpath('//android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.view.ViewGroup[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[2]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.webkit.WebView[1]/android.webkit.WebView[1]/android.view.View[1]/android.view.View[3]/android.view.View[1]/android.view.View[5]/android.view.View[2]').text
        return text

    @teststep
    def get_location(self):
        text = self.driver.find_element_by_xpath('//android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.view.ViewGroup[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[2]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.webkit.WebView[1]/android.webkit.WebView[1]/android.view.View[1]/android.view.View[3]/android.view.View[1]/android.view.View[7]/android.view.View[2]').text
        return text

    @teststep
    def judge_school_name(self):
        for i,j in enumerate(schoolName):
            self.input_school_name(j[0])
            for index,x in enumerate(schoolNickname):
                self.input_nickname(x[0])
                self.click_application()
                time.sleep(1.5)
                if j[1] == self.get_school_name():
                    if x[1] == self.get_school_nickname():
                        if self.get_location() == '请选择区域':
                            print('✅提示正确')
                            time.sleep(0.5)
                        else:
                            print('❌error:提示异常，请进行检查')
                    else:
                        print('❌error:提示异常，请进行检查')
                else:
                    print('❌error:提示异常，请进行检查')

    @teststep
    def click_the_arrow(self):
        self.driver.find_element_by_xpath('//*[@text=""]').click()
        print('点击 下拉箭头')
        time.sleep(0.5)

    @teststep
    def click_province(self):
        self.driver.find_element_by_xpath('//android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.view.ViewGroup[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[2]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.webkit.WebView[1]/android.webkit.WebView[1]/android.view.View[2]/android.view.View[2]/android.view.View[2]/android.view.View[1]/android.view.View[3]/android.view.View[3]').click()
        print('选择省份 河北省')
        time.sleep(5)

    @teststep
    def click_city(self):
        self.driver.find_element_by_xpath('//android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.view.ViewGroup[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[2]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.webkit.WebView[1]/android.webkit.WebView[1]/android.view.View[2]/android.view.View[2]/android.view.View[2]/android.view.View[2]/android.view.View[3]/android.view.View[6]').click()
        print('点击城市 保定市')
        time.sleep(5)

    @teststep
    def click_county(self):
        self.driver.find_element_by_xpath('//android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.view.ViewGroup[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[2]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.webkit.WebView[1]/android.webkit.WebView[1]/android.view.View[2]/android.view.View[2]/android.view.View[2]/android.view.View[3]/android.view.View[3]/android.view.View[23]').click()
        print('点击县级市 高碑店')
        time.sleep(5)

    @teststep
    def choose_lacation(self):
        time.sleep(2)
        x = [180,535,900]
        y = [1570,1775,1775]
        for i,j in enumerate([15,5,20]):
            for _ in range(j):
                click_bounds(self,x[i],y[i])
                time.sleep(0.1)
        time.sleep(1)

    @teststep
    def click_cancel(self):
        self.driver.find_element_by_xpath('//android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.view.ViewGroup[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[2]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.webkit.WebView[1]/android.webkit.WebView[1]/android.view.View[2]/android.view.View[2]/android.view.View[1]/android.view.View[1]').click()
        print('点击 取消')

    @teststep
    def click_ensure(self):
        self.driver.find_element_by_xpath('//*[@resource-id="weui-picker-confirm"]').click()
        print('点击 确定')
        time.sleep(2)

    @teststep
    def click_application(self):
        # self.driver.find_element_by_xpath('//*[@text="申请新建"]').click()
        click_bounds(self,500,980)
        print('点击 申请新建')
        time.sleep(1.5)

    @teststep
    def judge_tips_in_submit(self):
        tips_info =  self.driver.find_element_by_xpath(
            '//*[@text="提示：请填写需要新增的学校信息并提交，我们将在2个工作日内与您联系，确认后为您开通新学校。如在使用过程中遇到问题，请联系客服【微信公众号：在线助教】"]').text
        if tips_info == '提示：请填写需要新增的学校信息并提交，我们将在2个工作日内与您联系，确认后为您开通新学校。如在使用过程中遇到问题，请联系客服【微信公众号：在线助教】':
            print('✅tips正常')
        else:
            print('\n\t❌error:提示错误，请进行检查\n')

    @teststep
    def judge_tips_in_result(self,name='xxh高级中学',nickname='xxh',location='河北省 - 保定市 - 高碑店市'):
        info_ele = self.driver.find_elements_by_xpath('//*[@resource-id="app"]/android.view.View[3]/android.view.View')
        info_list = [i.text for i in info_ele]
        print(info_list)
        if '提交成功!' in str(info_list) \
                and '学校信息申请已提交，我们将在2个工作日内核实并为您开通。如有疑问，请联系客服【微信公众号：在线助教】' in str(info_list) \
            and name in str(info_list) \
            and nickname in str(info_list) \
            and location in str(info_list) \
            and '信息有误？立即修改' in str(info_list):
            print('✅页面信息正确')
        else:
            print('\n\t❌error:提示存在问题，请进行检查\n',info_list)

    @teststep
    def click_modify(self):
        self.driver.find_element_by_xpath('//android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.view.ViewGroup[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[2]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.webkit.WebView[1]/android.webkit.WebView[1]/android.view.View[1]/android.view.View[3]/android.view.View[10]').click()
        print('点击 信息有误，立即修改')
        time.sleep(1)

    @teststep
    def get_new_school(self):
        info_ele = self.driver.find_elements_by_xpath('//*[@resource-id="app"]/android.view.View[2]/android.view.View[1]/android.view.View[3]/android.view.View')[1:]
        info_list = str([i.text for i in info_ele])
        print('学校信息：',info_list)
        if '' in info_list and '' in info_list:
            print('✅创建学校申请成功')
        else:
            print('\n\t❌error:创建学校异常 请进行检查\n')
        time.sleep(2)

    @teststep
    def click_back(self):
        self.driver.find_element_by_xpath('//*[@resource-id="app"]/android.view.View[1]').click()
        print('点击 返回')
        time.sleep(1)