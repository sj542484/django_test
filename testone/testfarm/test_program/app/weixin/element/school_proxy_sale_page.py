import datetime
import re
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from testfarm.test_program.conf.decorator import teststep, teststeps
from testfarm.test_program.conf.basepage import BasePage
from testfarm.test_program.utils.click_bounds import click_bounds
from testfarm.test_program.app.weixin.test_data.phone_list import PhoneList

class SchoolProxySalePage(BasePage):
    @teststep
    def click_proxy_sale(self):
        self.driver.find_element_by_xpath('//*[@text="代退账号"]').click()
        time.sleep(2)

    @teststeps
    def wait_sale_page(self):
        try:
            ele = (By.XPATH, '//*[@text="代退账号"]')
            WebDriverWait(self.driver, 5, 0.3).until(EC.presence_of_element_located(ele))
            return True
        except:
            return False

    @teststeps
    def wait_refund_success_page(self):
        try:
            ele = (By.XPATH, '//*[@text="退款成功"]')
            WebDriverWait(self.driver, 5, 0.3).until(EC.presence_of_element_located(ele))
            return True
        except:
            return False

    @teststep
    def get_page_info(self):
        ele_info = self.driver.find_element_by_xpath('//android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.view.ViewGroup[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[2]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.webkit.WebView[1]/android.webkit.WebView[1]/android.view.View[1]/android.view.View[3]').text
        if ele_info == '输入手机号，查询学生的订单情况，点击【退款】可代学生退掉通过"代买账号"购得的学习卡。':
            print('✅页面提示正常')
        else:
            print('❌error:页面提示异常，请进行检查')

    @teststep
    def click_back(self):
        self.driver.find_element_by_xpath('//*[@text="返回"]').click()

    @teststep
    def input_stu_phone(self,phone_number):
        self.driver.find_element_by_xpath('//android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.view.ViewGroup[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[2]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.webkit.WebView[1]/android.webkit.WebView[1]/android.view.View[1]/android.view.View[4]/android.widget.EditText[1]').send_keys(phone_number)

    @teststep
    def click_search(self):
        click_bounds(self,910,685)
        time.sleep(2)

    @teststep
    def get_tips(self):
        time.sleep(0.5)
        tips = self.driver.find_element_by_xpath(
            '//android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.view.ViewGroup[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[2]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.webkit.WebView[1]/android.webkit.WebView[1]/android.view.View[2]').text
        return tips

    @teststep
    def get_stu_info(self):
        ele_list = self.driver.find_elements_by_xpath('//android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.view.ViewGroup[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[2]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.webkit.WebView[1]/android.webkit.WebView[1]/android.view.View[1]/android.view.View[5]/android.view.View[1]/android.view.View')
        ele_info = [i.text for i in ele_list]
        print(ele_info)
        return ele_info

    @teststep
    def get_order(self):
        '''订单条数'''
        ele_list = self.driver.find_elements_by_xpath('//android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.view.ViewGroup[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[2]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.webkit.WebView[1]/android.webkit.WebView[1]/android.view.View[1]/android.view.View')[8:]
        return len(ele_list)

    @teststep
    def get_num_in_page(self):
        '''页面中显示的数量'''
        info = self.driver.find_element_by_xpath('//android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.view.ViewGroup[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[2]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.webkit.WebView[1]/android.webkit.WebView[1]/android.view.View[1]/android.view.View[8]').text
        num = int(re.findall('\d+',info)[0])
        return num

    @teststep
    def no_num(self):
        '''订单列表中的不可退订单数量'''
        page_sourse = self.driver.page_source
        num = page_sourse.count('不可退费')
        return num

    @teststep
    def click_first_order(self):
        '''上一个脚本下单，这个第一条就是可退订单'''
        self.driver.find_element_by_xpath('//android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.view.ViewGroup[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[2]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.webkit.WebView[1]/android.webkit.WebView[1]/android.view.View[1]/android.view.View[9]').click()
        time.sleep(1)

    @teststep
    def gete_all_class(self):
        class_ele = self.driver.find_elements_by_xpath('//android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.view.ViewGroup[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[2]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.webkit.WebView[1]/android.webkit.WebView[1]/android.view.View[1]/android.view.View[7]/android.view.View')[1:]
        class_info = [i.text for i in class_ele]
        print('班级信息列表：',class_info)

    @teststep
    def click_second_order(self):
        '''第二个是不可取消订单'''
        self.driver.find_element_by_xpath('//android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.view.ViewGroup[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[2]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.webkit.WebView[1]/android.webkit.WebView[1]/android.view.View[1]/android.view.View[10]').click()
        time.sleep(1)

    @teststep
    def get_refundable_amount(self):
        try:
            ele = (By.XPATH, '//*[@text="可退金额￥0（0天）"]')
            WebDriverWait(self.driver, 5, 0.3).until(EC.presence_of_element_located(ele))
            print('✅显示金额正常')
        except:
            print('❌error:显示金额异常，请进行检查')


    @teststep
    def click_refund(self):
        # self.driver.find_element_by_xpath('//*[@text="退款"]').click()
        click_bounds(self,705,1560)
        time.sleep(1)

    @teststep
    def click_cancel(self):
        self.driver.find_element_by_xpath('//*[@text="取消"]').click()
        time.sleep(1)

    @teststep
    def input_pwd(self,text='请输入密码'):
        pwd_ele = self.driver.find_element_by_xpath('//*[@text="{}"]'.format(text))
        return pwd_ele

    @teststep
    def click_hide(self):
        self.driver.find_element_by_xpath('//*[@text=""]').click()
        time.sleep(0.3)

    @teststep
    def forget_pwd(self):
        self.driver.find_element_by_xpath('//*[@text="忘记密码？"]').click()
        time.sleep(1)

    @teststep
    def click_ensure(self):
        # ele = self.driver.find_element_by_xpath('//*[@text="确定"]')
        click_bounds(self,720,1300)
        time.sleep(1)

    @teststep
    def get_tips_null(self):
        info = self.driver.find_element_by_xpath('//*[@resource-id="app"]/android.view.View[18]/android.view.View[4]/android.view.View[2]').text
        if info == '请输入密码':
            print('✅没有输入密码 提示正常')
        else:
            print('❌error:没有输入密码,提示异常,请进行检查')

    @teststep
    def get_error_tips(self):
        try:
            ele = (By.XPATH, '//*[@text="手机号或密码错误"]')
            WebDriverWait(self.driver, 5, 0.3).until(EC.presence_of_element_located(ele))
            info = ele.text
            if info == '手机号或密码错误':
                print('✅输入错误密码，提示正常')
            else:
                print('❌error:输入错密码，提示异常，请进行检查')
        except:
            return False

    @teststep
    def expect_data(self, data_before):
        data = datetime.date(*map(int, data_before.split('-')))
        last_monday = (data + datetime.timedelta(days= -31)).strftime('%Y-%m-%d')
        return last_monday

    @teststep
    def judge_phone(self):
        for i in PhoneList[:-1]:
            self.input_stu_phone(i[0])
            self.click_search()
            tips = self.get_tips()
            if tips == i[1]:
                print('✅搜索学生提示正确')
            else:
                print('❌error:搜索学生提示异常，请进行检查')

    @teststep
    def get_order_info(self):
        ele_list = self.driver.find_elements_by_xpath('//android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.view.ViewGroup[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[2]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.webkit.WebView[1]/android.webkit.WebView[1]/android.view.View[1]/android.view.View')[-1]
        info =[i.text for i in  ele_list.find_elements_by_xpath('./android.view.View')[:-1]]
        print('订单详情：',info)