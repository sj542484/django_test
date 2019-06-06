from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from testfarm.test_program.conf.decorator import teststep, teststeps
from testfarm.test_program.conf.basepage import BasePage
from testfarm.test_program.utils.click_bounds import click_bounds
import time

class TeacherManage(BasePage):
    '''教师管理页面'''

    @teststeps
    def wait_teacher_manage_page(self):
        '''是否进入老师管理界面'''
        try:
            ele = (By.XPATH, '//*[@text="小玉5.21测试"]')
            WebDriverWait(self.driver, 20, 0.5).until(EC.presence_of_element_located(ele))
            return True
        except:
            return False

    @teststeps
    def wait_teacher_manage_page_class(self):
        '''是否进入老师管理界面'''
        try:
            ele = (By.XPATH, '//*[@text="小玉老师666666（小玉老师666666） 已入校 1个班级；1个学生"]')
            WebDriverWait(self.driver, 20, 0.5).until(EC.presence_of_element_located(ele))
            return True
        except:
            return False

    @teststeps
    def wait_change_classes_page(self):
        '''是否进入老师管理界面'''
        try:
            ele = (By.XPATH, '//*[@text="转班操作"]')
            WebDriverWait(self.driver, 20, 0.5).until(EC.presence_of_element_located(ele))
            return True
        except:
            return False

    @teststeps
    def wait_tea_class_page(self):
        '''是否进入老师管理界面'''
        try:
            ele = (By.XPATH, '//*[@text="李老师班级"]')
            WebDriverWait(self.driver, 20, 0.5).until(EC.presence_of_element_located(ele))
            return True
        except:
            return False

    @teststeps
    def wait_teacher_info_page(self):
        '''是否进入老师管理界面'''
        try:
            ele = (By.XPATH, '//*[@text="老师详情"]')
            WebDriverWait(self.driver, 20, 0.5).until(EC.presence_of_element_located(ele))
            return True
        except:
            return False

    @teststeps
    def wait_creat_tea_page(self):
        '''是否进入老师管理界面'''
        try:
            ele = (By.XPATH, '//*[@text="创建老师-小玉5.21测试"]')
            WebDriverWait(self.driver, 20, 0.5).until(EC.presence_of_element_located(ele))
            return True
        except:
            return False

    @teststeps
    def wait_preview_page(self):
        '''是否进入老师管理界面'''
        try:
            ele = (By.XPATH, '//android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.view.ViewGroup[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[2]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.webkit.WebView[1]/android.webkit.WebView[1]/android.view.View[1]/android.view.View[3]/android.view.View[1]')
            WebDriverWait(self.driver, 10, 0.5).until(EC.presence_of_element_located(ele))
            return True
        except:
            return False

    @teststeps
    def wait_jump_page(self):
        '''是否进入老师管理界面'''
        try:
            ele = (By.XPATH,'//*[@resource-id="btn-open"]')
            WebDriverWait(self.driver, 10, 0.5).until(EC.presence_of_element_located(ele))
            return True
        except:
            return False

    @teststeps
    def wait_succeed_page(self):
        '''是否进入老师管理界面'''
        try:
            ele = (By.XPATH, '//*[@text="提交成功!"]')
            WebDriverWait(self.driver, 10, 0.5).until(EC.presence_of_element_located(ele))
            return True
        except:
            return False

    @teststep
    def get_all_teacher(self):
        '''获取全部老师及班级信息'''
        ele_list = self.driver.find_elements_by_xpath('//android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.view.ViewGroup[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[2]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.webkit.WebView[1]/android.webkit.WebView[1]/android.view.View[1]/android.view.View[2]/android.view.View[3]/android.view.View')[1:-1]
        info_list = [i.text for i in ele_list ]
        print(info_list)
        return info_list,ele_list

    @teststep
    def click_invite_tea(self):
        self.driver.find_element_by_xpath('//*[@resource-id="app"]/android.view.View[3]/android.view.View[1]/android.view.View[1]').click()
        print('点击 邀请老师')
        time.sleep(1)

    @teststep
    def click_create_group(self):
        self.driver.find_element_by_xpath('//*[@resource-id="app"]/android.view.View[3]/android.view.View[2]/android.view.View[1]').click()
        print('点击 创建分组')
        time.sleep(1)

    @teststep
    def get_info(self):
        '''获取界面提示文字'''
        tip_top = self.driver.find_element_by_xpath('//*[@text="批量输入（老师姓名+空格+手机号，可以复制黏贴哦）"]').text
        tip_middle = self.driver.find_element_by_xpath('//*[@text="粘贴老师信息，自动识别姓名及手机号，如：王某某 15200000000 一行一位老师，记得换行哦"]').text
        tip_bottle = self.driver.find_element_by_xpath('//*[@text="【姓名 + 空格 + 手机号】如：王某某 15200000000 ；一行一人，输入完成后，点击【预览】，检查所输入内容"]').text
        if tip_top == '批量输入（老师姓名+空格+手机号，可以复制黏贴哦）':
            if tip_middle == '粘贴老师信息，自动识别姓名及手机号，如：王某某 15200000000 一行一位老师，记得换行哦':
                if tip_bottle == '【姓名 + 空格 + 手机号】如：王某某 15200000000 ；一行一人，输入完成后，点击【预览】，检查所输入内容':
                    print('✅提示词正确')
                else:
                    print('\n\t❌error:提示词错误，请进行检查\n')
            else:
                print('\n\t❌error:提示词错误，请进行检查\n')
        else:
            print('\n\t❌error:提示词错误，请进行检查\n')

    @teststep
    def input_tea_info(self):
        self.driver.find_element_by_xpath('//*[@text="粘贴老师信息，自动识别姓名及手机号，如：王某某 15200000000 一行一位老师，记得换行哦"]').send_keys('时晓 1311111111\n小时 1333333333')
        print('输入老师信息')

    @teststep
    def click_preview(self):
        # self.driver.find_element_by_xpath('//*[@text="预览"]').click()
        click_bounds(self,520,1420)
        print('点击 预览')
        time.sleep(1)

    @teststep
    def check_tips(self):
        try:
            ele = (By.XPATH, '//*[@text="请输入正确手机号"]')
            WebDriverWait(self.driver, 10, 0.5).until(EC.presence_of_element_located(ele))
            return True
        except:
            return False

    @teststep
    def completion_phone_top(self):
        self.driver.find_element_by_xpath('//*[@text="1311111111"]').send_keys('13111111113')

    @teststep
    def hide_key_board(self):
        click_bounds(self,960,1325)
        print('关闭小键盘')
        time.sleep(0.3)

    @teststep
    def completion_phone_bottom(self):
        self.driver.find_element_by_xpath('//*[@text="1333333333"]').send_keys('13333333333')

    @teststep
    def change_name(self):
        self.driver.find_element_by_xpath('//*[@text="小时"]').send_keys('xxh')

    @teststep
    def click_invite_ensure(self):
        # self.driver.find_element_by_xpath('//*[@text="邀请老师"]').click()
        click_bounds(self,520,1950)
        print('点击 邀请老师')
        time.sleep(2)

    @teststep
    def succeed_info(self):
        succeed_info = self.driver.find_element_by_xpath('//*[@text="提交成功!"]').text
        tips_info = self.driver.find_element_by_xpath('//*[@text="您已向 2 名老师发送邀请，老师用对应手机号注册在线助教并“加入学校”即可完成操作。请如有疑问，请联系客服【微信公众号：在线助教】"]').text
        tea_one = self.driver.find_element_by_xpath('//*[@text="时晓 (13111111113)"]').text
        tea_two = self.driver.find_element_by_xpath('//*[@text="xxh (13333333333)"]').text
        print(succeed_info,'\n',tips_info)
        print(tea_one,'\t',tea_two)
        print('✅操作成功')
        time.sleep(2)

    @teststep
    def click_back(self):
        self.driver.find_element_by_xpath('//*[@resource-id="app"]/android.view.View[1]').click()
        print('点击 返回')
        time.sleep(1)

    @teststep
    def click_here(self):
        self.driver.find_element_by_xpath('//*[@text="点击这里"]').click()
        print('点击 点击这里')

    @teststep
    def change_name_in_tea_info(self):
        self.driver.find_element_by_xpath('//*[@text="xxh"]').send_keys('小时')
        print('点击 修改姓名')
        time.sleep(1)

    @teststep
    def get_tea_name(self):
        tea_name = self.driver.find_element_by_xpath('//android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.view.ViewGroup[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[2]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.webkit.WebView[1]/android.webkit.WebView[1]/android.view.View[1]/android.view.View[3]/android.view.View[2]/android.view.View[2]/android.view.View[2]/android.widget.EditText[1]').text
        print('tea_name:',tea_name)
        return tea_name

    @teststep
    def save_change(self):
        # self.driver.find_element_by_xpath('//*[@text="保存修改"]').click()
        click_bounds(self,530,1020)
        print('点击 保存修改')
        time.sleep(1)

    @teststep
    def invite_cancel(self):
        # self.driver.find_element_by_xpath('//*[@text="取消邀请"]').click()
        click_bounds(self,530,1200)
        print('点击 取消邀请')
        time.sleep(1)

    @teststep
    def click_ensure(self):
        # self.driver.find_element_by_xpath('//*[@text="确定"]').click()
        click_bounds(self,720,1200)
        print('点击 确定')
        time.sleep(1)

    @teststep
    def click_cancel(self):
        self.driver.find_element_by_xpath('//*[@text="取消"]').click()
        print('点击 取消')
        time.sleep(1)

# =============================== 老师详情 =======================================

    @teststep
    def class_list(self):
        class_ele_list = self.driver.find_elements_by_xpath('//android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.view.ViewGroup[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[2]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.webkit.WebView[1]/android.webkit.WebView[1]/android.view.View[1]/android.view.View[3]/android.view.View[3]/android.view.View')[1:-1]
        class_list = [i.text for i in class_ele_list]
        print('班级列表：',class_list)
        return class_ele_list,class_list

    @teststep
    def get_tea_info(self):
        tea_ele_list = self.driver.find_elements_by_xpath('//android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.view.ViewGroup[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[2]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.webkit.WebView[1]/android.webkit.WebView[1]/android.view.View[1]/android.view.View[3]/android.view.View[1]/android.view.View[2]/android.view.View[1]/android.view.View[1]/android.view.View')
        tea_info = [i.text for i in tea_ele_list]
        print('教师详情：',tea_info)

    @teststep
    def class_info(self):
        class_info = self.driver.find_element_by_xpath('//android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.view.ViewGroup[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[2]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.webkit.WebView[1]/android.webkit.WebView[1]/android.view.View[1]/android.view.View[3]/android.view.View[1]').text
        # print('班级详情：',class_info)

    @teststep
    def stu_info(self):
        ele_list = self.driver.find_elements_by_xpath('//android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.view.ViewGroup[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[2]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.webkit.WebView[1]/android.webkit.WebView[1]/android.view.View[1]/android.view.View[3]/android.view.View[2]/android.view.View')[1:-1]
        info_list = [i.text for i in ele_list]
        # print('学生详情：',info_list)

# =========================== 转班操作 ==================================
    @teststep
    def click_change_classes(self):
        # self.driver.find_element_by_xpath('//*[@text="转班"]').click()
        click_bounds(self,560,1960)
        print('点击 转班')
        time.sleep(1)

    @teststep
    def show_class_info(self):
        ele_list = self.driver.find_elements_by_xpath('//android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.view.ViewGroup[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[2]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.webkit.WebView[1]/android.webkit.WebView[1]/android.view.View[1]/android.view.View[3]/android.view.View[1]/android.view.View[2]/android.view.View')
        info_list = [i.text for i in ele_list]
        print('班级基本情况：',info_list)

    @teststep
    def all_tea_to_change(self):
        ele_list = self.driver.find_elements_by_xpath('//android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.view.ViewGroup[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[2]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.webkit.WebView[1]/android.webkit.WebView[1]/android.view.View[1]/android.view.View[3]/android.view.View[3]/android.view.View')[1:-1]
        info_list = [i.text for i in ele_list]
        # print('可接手的老师列表：',info_list)
        return ele_list

    @teststep
    def click_ensure_change(self):
        # self.driver.find_element_by_xpath('//*[@text="确定转班"]').click()
        click_bounds(self,900,520)
        print('点击 确认转班')
        time.sleep(1)

    @teststep
    def input_pwd(self):
        self.driver.find_element_by_xpath('//*[@text="请输入密码"]').send_keys('123321')
        print('输入密码')

    @teststep
    def click_ensure_pwd(self):
        click_bounds(self,730,850)
        print('点击 确定')