from selenium.webdriver.support.wait import WebDriverWait

from testfarm.test_program.conf.decorator import teststep
from testfarm.test_program.conf.basepage import BasePage
from testfarm.test_program.utils.click_bounds import click_bounds
from selenium.webdriver.common.by import By
import time
import re

class Statement(BasePage):
    '''对账单页面'''
    @teststep
    def wait_check_page(self):
        """以“title:重置密码”的xpath @text为依据"""
        locator = (By.XPATH, '//*[@text="对账单"]')
        try:
            WebDriverWait(self.driver, 20, 0.5).until(lambda x: x.find_element(*locator))
            return True
        except:
            return False

    def click_statement(self):
        # 点击对账单
        self.driver.find_element_by_xpath('//*[@text="对账单"]').click()
        print('点击对账单')
        time.sleep(2)

    def show_statement_num_wait(self):
        locator = (By.XPATH, '//*[@text="当前提分版人数"]')
        try:
            WebDriverWait(self.driver, 20, 0.5).until(lambda x: x.find_element(*locator))
            return True
        except:
            return False

    def show_statement_num(self):
        # 判断进入对账单页面
        num = self.driver.find_element_by_xpath('//*[@text="6"]').text
        ele = self.driver.find_element_by_xpath('//*[@text="当前提分版人数"]').text
        number_of_trials = self.driver.find_element_by_xpath('//*[@text="其中试用人数:0"]').text
        if ele == "当前提分版人数":
            print("进入对账单页面成功,当前提分班人数%s,试用人数显示%s"%(num,number_of_trials))
        else:
            print("进入对账单页面失败")

    def show_month_price(self):
        # 显示本月的总额
        time.sleep(1)
        a1 = self.driver.find_element_by_xpath('//*[@resource-id="app"]/android.view.View[3]/android.view.View[3]/android.view.View[5]').text
        aa1= re.findall(r'\d+\.\d+', a1)
        a1 = float(aa1[0])  # 0.08
        # print(a1,type(a1))

        a2 = self.driver.find_element_by_xpath('//*[@resource-id="app"]/android.view.View[3]/android.view.View[3]/android.view.View[6]').text
        aa1= re.findall(r'\d+\.\d+', a2)
        a2 = float(aa1[0])  # 0.08
        # print(a2)

        a3 = self.driver.find_element_by_xpath('//*[@resource-id="app"]/android.view.View[3]/android.view.View[3]/android.view.View[7]').text
        aa1= re.findall(r'\d+\.\d+', a3)
        a3 = float(aa1[0])  # 0.08
        # print(a3)
        print("本月的总额，预计结算金额，预计万星返款分别是：",a1,a2,a3)
        num = a2 + a3
        if a1 == num:
            print("✅对账单数据正确")
        else:
            print("❌error:对账单数据异常，请进行检查")
        return a1

    def show_school_money(self):
        # 显示学校余额
        time.sleep(1)
        ele = self.driver.find_element_by_xpath("//android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.view.ViewGroup[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[2]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.webkit.WebView[1]/android.webkit.WebView[1]/android.view.View[1]/android.view.View[5]/android.view.View[2]/android.view.View[2]").text
        print("学校余额是",ele)
        return float(ele.replace('￥','').replace(',',''))

    def show_more_data(self):
        # 显示更多的数据
        time.sleep(2)
        ele = self.driver.find_element_by_xpath('//*[@text="查询更多数据"]').text
        if ele == "查询更多数据":
            print("进入查看更多数据")
            money = self.driver.find_element_by_xpath('//android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.view.ViewGroup[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[2]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.webkit.WebView[1]/android.webkit.WebView[1]/android.view.View[1]/android.view.View[5]/android.view.View[2]/android.view.View[2]').text
            print("学校的余额是：%s"%money)

    def click_enter_bill(self):
        # 点击进入账单
        self.driver.find_element_by_xpath('//*[@text="对账单"]').click()
        # click_bounds(self,500,1500)
        time.sleep(2)

    def judge_enter_bill(self):
        # 判断是否进入账单
        locator = (By.XPATH, '//*[@resource-id="app"]/android.view.View[3]/android.widget.ListView[1]/android.view.View[1]/android.view.View[1]')
        try:
            WebDriverWait(self.driver, 20, 0.5).until(lambda x: x.find_element(*locator))
            print('进入账单成功')
            return True
        except:
            print('进入账单失败')
            return False

    @teststep
    def get_all_order(self):
        page = self.driver.page_source
        pat = re.compile(r'text="(.*?)"')
        c = pat.findall(page)
        all_order = [i for i in c if i][6:-1]
        step = 3
        t = [all_order[i:i + step] for i in range(0, len(all_order), step)]
        data = [[j.strip() for j in '\xa0\xa0'.join([x.strip() for x in i]).split('\xa0\xa0')] for i in t]
        return data

    @teststep
    def get_first_order(self):
        ele_list = self.driver.find_elements_by_xpath('//android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.view.ViewGroup[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[2]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.webkit.WebView[1]/android.webkit.WebView[1]/android.view.View[1]/android.view.View[3]/android.widget.ListView[1]/android.view.View[1]/android.view.View')
        info_list = [i.text for i in ele_list]
        print('订单信息：',info_list)
        return info_list

    def change_time(self):
        # 更改时间
        self.driver.find_element_by_xpath('//*[@resource-id="app"]/android.view.View[3]/android.view.View[1]/android.view.View[2]').click()
        time.sleep(2)

    def click_determine(self):
        time.sleep(1)
        # 点击确定
        click_bounds(self, 980, 1390)
        print('点击 确定')

    def click_student_select(self):
        # 点击学生交费查询
        time.sleep(1)
        self.driver.find_element_by_xpath('//android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.view.ViewGroup[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[2]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.webkit.WebView[1]/android.webkit.WebView[1]/android.view.View[1]/android.view.View[5]/android.view.View[4]').click()

    def judge_select(self):
        # 判断是否进入学生交费查询
        locator = (By.XPATH, '//*[@text="请输入学生手机号/昵称"]')
        try:
            WebDriverWait(self.driver, 20, 0.5).until(lambda x: x.find_element(*locator))
            return True
        except:
            return False

    def get_input(self):
        # 输入学生手机号
        ele = self.driver.find_element_by_xpath('//*[@text="请输入学生手机号/昵称"]')
        return ele

    def get_tips(self):
        ele = self.driver.find_element_by_xpath('//android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.view.ViewGroup[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[2]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.webkit.WebView[1]/android.webkit.WebView[1]/android.view.View[2]')
        return ele

    def ensure_seach(self):
        # 点击搜索
        ele = self.driver.find_element_by_xpath('//*[@resource-id="app"]/android.view.View[1]/following-sibling::android.view.View[2]/android.view.View')
        return ele

    def judge_select_error(self):
        # 判断是否进入学生交费查询
        # 判断是否进入学生交费查询
        locator = (By.XPATH, '//*[@text="请输入学生手机号/昵称"]')
        try:
            WebDriverWait(self.driver, 20, 0.5).until(lambda x: x.find_element(*locator))
            return True
        except:
            return False

    def show_student(self,stu_phone):
        # 显示交费同学姓名
        time.sleep(2)
        ele = self.driver.find_element_by_xpath('//android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.view.ViewGroup[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[2]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.webkit.WebView[1]/android.webkit.WebView[1]/android.view.View[1]/android.view.View[4]/android.view.View[2]')
        info = ele.text
        if stu_phone in info:
            if '基础' in info:
                print('✅学生信息正确，学生信息为：%s'%info)
            elif '试用' in info and '试用期至' in info:
                print('✅学生信息正确，学生信息为：%s'%info)
            elif '提分版' in info and '有效期至' in info:
                print('✅学生信息正确，学生信息为：%s'%info)
            else:
                print('❌error:学生无版本标志，请进行检查，学生信息为：%s'%info)
        else:
            print('❌error:学生信息错误，请进行检查，学生信息为：%s,学生手机号为：%s'%(info,stu_phone))
        ele.click()
        print('点击进入学生详情页')
        time.sleep(2)

    def check_student_deail(self):
        # 查看学生详情
        sta = 0
        ele = self.driver.find_element_by_xpath('//*[@resource-id="app"]')
        l = ele.find_elements(By.CLASS_NAME, 'android.view.View')
        info = [i.text for i in l]
        step = 6
        data = [info[i + 11:i + 15] for i in range(0, len(info[11:]), step)]
        for i in data:
            if len(i) != 4:
                print('❌error:数据错误，请进行检查，数据为：%s'%i)
                sta += 1
        if sta == 0:
            print('✅每条数据均由4条信息构成')

    def click_class_money(self):
        #  点击班级交费
        time.sleep(1)
        self.driver.find_element_by_xpath('//android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.view.ViewGroup[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[2]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.webkit.WebView[1]/android.webkit.WebView[1]/android.view.View[1]/android.view.View[5]/android.view.View[5]').click()

    def judge_class_money(self):
        locator = (By.XPATH, '//*[@text="请输入班级名称/班号"]')
        try:
            WebDriverWait(self.driver, 20, 0.5).until(lambda x: x.find_element(*locator))
            return True
        except:
            return False

    def select_class_number(self):
        # 输入班级名称
        self.driver.find_element_by_xpath('//*[@text="请输入班级名称/班号"]').send_keys('9259')

    def select_class_error(self):
        # 输入班级名称
        self.driver.find_element_by_xpath('//*[@text="请输入班级名称/班号"]').send_keys("789")
        time.sleep(2)

    def enter_class(self):
        # 点击进入李老师班级
        self.driver.find_element_by_xpath('//*[@resource-id="app"]/android.view.View[5]').click()
        time.sleep(2)

    def judge_class_name(self):
        # 判断是否进入李老师班级
        time.sleep(3)
        ele = self.driver.find_element_by_xpath('//*[@text="李老师班级"]').text
        if ele == "李老师班级":
            print("进入李老师班级成功")
        else:
            print("error🌟🌟🌟----进入李老师班级失败")

    def show_class_num(self):
        #显示班级情况
        ele = self.driver.find_element_by_xpath('//*[@resource-id="app"]/android.view.View[4]')
        l = ele.find_elements(By.CLASS_NAME, 'android.view.View')[:-1]
        for i,j in enumerate(l[1:-1]):
            print(i,'\t',j.text)
        print('over')

    @teststep
    def get_error_info(self):
        locator = (By.XPATH, '//*[@text="本校无此学生"]')
        try:
            WebDriverWait(self.driver, 3, 0.3).until(lambda x: x.find_element(*locator))
            return True
        except:
            return False

    @teststep
    def click_doubt(self):
        self.driver.find_element_by_xpath('//*[@resource-id="app"]/android.view.View[3]/android.view.View[2]/android.view.View[1]/android.widget.Image[1]').click()
        time.sleep(1)

    @teststep
    def get_info(self):
        ele_list = self.driver.find_elements_by_xpath('//android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.view.ViewGroup[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[2]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.webkit.WebView[1]/android.webkit.WebView[1]/android.view.View[1]/android.view.View[7]/android.view.View')
        info = [i.text for i in ele_list]
        print('info',info)
        return info ,ele_list