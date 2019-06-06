import re
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from testfarm.test_program.conf.decorator import teststep, teststeps
from testfarm.test_program.conf.basepage import BasePage
from testfarm.test_program.utils.click_bounds import click_bounds

class SchoolProxyPage(BasePage):
    @teststep
    def click_proxy_buy(self):
        self.driver.find_element_by_xpath('//*[@text="代买账号"]').click()

    @teststeps
    def wait_buy_page(self):
        try:
            ele = (By.XPATH, '//*[@text="代买账号"]')
            WebDriverWait(self.driver, 5, 0.3).until(EC.presence_of_element_located(ele))
            return True
        except:
            return False

    @teststeps
    def wait_buy_success_page(self):
        try:
            ele = (By.XPATH, '//*[@resource-id="app"]/android.view.View[1]')
            WebDriverWait(self.driver, 5, 0.3).until(EC.presence_of_element_located(ele))
            return True
        except:
            return False

    @teststeps
    def wait_choose_stu_page(self):
        try:
            ele = (By.XPATH, '//*[@text="选择学生"]')
            WebDriverWait(self.driver, 5, 0.3).until(EC.presence_of_element_located(ele))
            return True
        except:
            return False

    @teststeps
    def wait_amount_input_page(self):
        try:
            ele = (By.XPATH, '//*[@text="批量输入"]')
            WebDriverWait(self.driver, 5, 0.3).until(EC.presence_of_element_located(ele))
            return True
        except:
            return False

    @teststeps
    def wait_choose_card_page(self):
        try:
            ele = (By.XPATH, '//*[@text="选择学习卡"]')
            WebDriverWait(self.driver, 5, 0.3).until(EC.presence_of_element_located(ele))
            return True
        except:
            return False

    @teststep
    def click_back(self):
        self.driver.find_element_by_xpath('//*[@text="返回"]').click()
        time.sleep(0.3)

    @teststep
    def click_this(self):
        self.driver.find_element_by_xpath('//*[@text="这里"]').click()

    @teststep
    def get_class_list(self):
        time.sleep(2)
        tea_one = self.driver.find_element_by_xpath('//*[@text="sff1134"]').text
        class_one = self.driver.find_elements_by_xpath('//android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.view.ViewGroup[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[2]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.webkit.WebView[1]/android.webkit.WebView[1]/android.view.View[1]/android.view.View[5]/android.view.View')[1:-1]
        class_one_info = [i.text for i in class_one]
        tea_two = self.driver.find_element_by_xpath('//*[@text="小玉老师666666"]').text
        class_two = self.driver.find_elements_by_xpath('//android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.view.ViewGroup[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[2]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.webkit.WebView[1]/android.webkit.WebView[1]/android.view.View[1]/android.view.View[7]/android.view.View')[1:-1]
        class_two_info = [i.text for i in class_two]
        print(' 教师：',tea_one,'\n\t班级：',class_one_info,'\n','教师：',tea_two,'\n\t班级：',class_two_info)

    @teststep
    def click_tea_li_class(self):
        self.driver.find_element_by_xpath('//android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.view.ViewGroup[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[2]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.webkit.WebView[1]/android.webkit.WebView[1]/android.view.View[1]/android.view.View[5]/android.view.View[2]').click()

    @teststep
    def get_stu(self):
        class_ele = self.driver.find_elements_by_xpath('//android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.view.ViewGroup[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[2]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.webkit.WebView[1]/android.webkit.WebView[1]/android.view.View[1]/android.view.View[4]/android.view.View')[1:-1]
        info_list = [i.text for i in class_ele]
        for i in class_ele:
            i.click()
            time.sleep(0.2)
        return class_ele

    @teststep
    def click_all(self):
        self.driver.find_element_by_xpath('//*[@resource-id="app"]/android.view.View[5]/android.view.View[2]/android.view.View[1]').click()
        time.sleep(0.5)

    @teststep
    def click_next(self):
        # self.driver.find_element_by_xpath('//*[@text="下一步"]').click()
        click_bounds(self,890,1970)
        time.sleep(1)

    @teststep
    def judge_tips_have_no_stu(self):
        info = self.driver.find_element_by_xpath('//*[@text="请先选择学生"]').text
        if info == '请先选择学生':
            print('✅没有选择学生，提示正确')
        else:
            print('❌error:没有选择学生，提示异常，请进行检查')

    @teststep
    def get_all_number(self):
        try:
            info = self.driver.find_element_by_xpath('//android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.view.ViewGroup[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[2]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.webkit.WebView[1]/android.webkit.WebView[1]/android.view.View[1]/android.view.View[5]/android.view.View[4]').text
            num = int(re.findall('\d+',info)[0])
        except:
            num = 0
        return num

    @teststep
    def get_all_card(self):
        card_ele_list = self.driver.find_elements_by_xpath('//android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.view.ViewGroup[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[2]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.webkit.WebView[1]/android.webkit.WebView[1]/android.view.View[1]/android.view.View[4]/android.view.View')[1:-1]
        card_info_list = [i.text for i in card_ele_list]
        return card_ele_list

    @teststep
    def get_cash(self):
        info = self.driver.find_element_by_xpath('//android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.view.ViewGroup[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[2]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.webkit.WebView[1]/android.webkit.WebView[1]/android.view.View[1]/android.view.View[5]/android.view.View[3]').text
        b = re.findall(r'\d+', info)
        res = '.'.join(b)
        return '%.2f'%float(res)

    @teststep
    def input_month(self):
        self.driver.find_element_by_xpath('//android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.view.ViewGroup[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[2]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.webkit.WebView[1]/android.webkit.WebView[1]/android.view.View[1]/android.view.View[4]/android.view.View[6]/android.widget.EditText[1]').send_keys('1')
        time.sleep(5)

    @teststep
    def input_daya(self):
        self.driver.find_element_by_xpath('//android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.view.ViewGroup[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[2]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.webkit.WebView[1]/android.webkit.WebView[1]/android.view.View[1]/android.view.View[4]/android.view.View[7]/android.widget.EditText[1]').send_keys('31')
        time.sleep(5)

    @teststep
    def input_pwd(self):
        try:
            ele = (By.XPATH, '//*[@text="请输入密码"]')
            WebDriverWait(self.driver, 5, 0.3).until(EC.presence_of_element_located(ele))
            self.driver.find_element_by_xpath('//*[@text="请输入密码"]').send_keys('123321')
            return True
        except:
            return False

    @teststep
    def click_ensure(self):
        # self.driver.find_element_by_xpath('//*[@text="确定"]').click()
        click_bounds(self,710,1030)
        time.sleep(2)

    @teststep
    def get_stu_info(self):
        ele_info = self.driver.find_elements_by_xpath('//android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.view.ViewGroup[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[2]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.webkit.WebView[1]/android.webkit.WebView[1]/android.view.View[1]/android.view.View[4]/android.view.View')[1:-1]
        info_list = [[j.text for j in i.find_elements_by_xpath('./android.view.View[1]')] for i in ele_info]
        print(info_list)

    @teststep
    def input_amount_phone(self,amount_phone,content='粘贴学生手机号，自动识别学生信息，一行一个学生手机号，记得换行哦！'):      # self.driver.find_element_by_xpath('//android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.view.ViewGroup[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[2]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.webkit.WebView[1]/android.webkit.WebView[1]/android.view.View[1]/android.view.View[4]/android.view.View[2]/android.view.View[2]/android.widget.EditText[1]').click()
        time.sleep(0.3)
        self.driver.find_element_by_xpath('\
        //android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.view.ViewGroup[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[2]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.webkit.WebView[1]/android.webkit.WebView[1]/android.view.View[1]/android.view.View[4]/android.view.View[2]/android.view.View[2]/android.widget.EditText[1]').send_keys(amount_phone)

    @teststep
    def click_warning(self):
        self.driver.find_element_by_xpath('//*[@text=""]').click()
        time.sleep(0.6)

    @teststep
    def click_have_card_tips(self):
        self.driver.find_element_by_xpath('//*[@text=""]').click()
        time.sleep(0.3)

    @teststep
    def get_warnning_text(self):
        expect_data = '手机号不符合规范'
        info = self.driver.find_element_by_xpath('//android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.view.ViewGroup[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[2]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.webkit.WebView[1]/android.webkit.WebView[1]/android.view.View[1]/android.view.View[9]/android.view.View[2]/android.view.View[1]').text
        if info == expect_data:
            print('✅手机号输入异常提示正确')
        else:
            print('❌error:手机号输入异常提示异常，请进行检查，页面显示信息为：%s,设定文本为：%s'%(info,expect_data))

    @teststep
    def click_quit(self):
        self.driver.find_element_by_xpath('//*[@text="×"]').click()
        time.sleep(0.3)

    @teststep
    def phone_error_tips(self):
        info = self.driver.find_element_by_xpath('//android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.view.ViewGroup[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[2]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.webkit.WebView[1]/android.webkit.WebView[1]/android.view.View[1]/android.view.View[5]').text
        if info == '预览: 共识别3个号码/1个号码错误':
            print('✅手机号判别正确')
        else:
            print('❌error:手机号判别异常，请进行检查')

    @teststep
    def stu_not_in_school(self):
        info = self.driver.find_element_by_xpath('//android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.view.ViewGroup[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[2]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.webkit.WebView[1]/android.webkit.WebView[1]/android.view.View[1]/android.view.View[7]/android.view.View[2]/android.view.View[1]')
        if info == '非本校学生账号':
            print('✅非本校学生，提示正常')
        else:
            print('❌error;非本校学生，提示异常，请进行检查')

    @teststep
    def stu_card_info(self):
        info = self.driver.find_element_by_xpath('//android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.view.ViewGroup[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[2]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.webkit.WebView[1]/android.webkit.WebView[1]/android.view.View[1]/android.view.View[4]/android.view.View[2]/android.widget.CheckBox[1]').text
        info = info.split(' ')
        stu_name = info[1]
        stu_phone = info[3]
        validity = info[5][4:]
        print('学生姓名：{}，学生手机号：{}，有效期至：{}'.format(stu_name,stu_phone,validity))
        return validity

    @teststep
    def choose_first_stu(self):
        self.driver.find_element_by_xpath('//android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.view.ViewGroup[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[2]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.webkit.WebView[1]/android.webkit.WebView[1]/android.view.View[1]/android.view.View[4]/android.view.View[2]').click()