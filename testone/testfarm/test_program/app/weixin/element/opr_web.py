from selenium import webdriver
from testfarm.test_program.conf.base_config import GetVariable
import time

class OprWeb():
    def __init__(self,type,phone=None,code=None):
        self.driver = webdriver.Chrome()
        self.type = type
        self.data = GetVariable()
        self.phone_number = phone
        self.code = code

    def management_login(self):
        '''登陆 到 指定界面'''
        self.driver.get(self.data.MANAGEMENT_URL)
        time.sleep(1.5)
        self.driver.maximize_window()
        time.sleep(0.5)
        self.driver.find_element_by_id('v_username').send_keys(self.data.MANAGEMENT_ACCOUNT)
        time.sleep(0.3)
        self.driver.find_element_by_id('v_passwd').send_keys(self.data.MANAGEMENT_PWD)
        time.sleep(0.3)
        self.driver.find_element_by_id('v_login').click()
        time.sleep(3.5)
        self.driver.find_element_by_xpath('//a[@base-url="{}"]'.format(self.type['department'])).click()
        time.sleep(1)
        self.driver.find_element_by_xpath(
            '//a[@base-url="{}"]/following-sibling::ul/li[{}]'.format(self.type['department'],self.type['opr_type'])).click()
        time.sleep(2)

    def get_info(self):
        '''获取验证码'''
        self.driver.find_element_by_xpath('//*[@id="doc-main"]/div/div/div/div/div[1]/input').send_keys(self.phone_number)
        time.sleep(0.3)
        self.driver.find_element_by_xpath("//button[@ng-click=\"send('{}','{}')\"]".format(self.code[0],self.code[1])).click()
        time.sleep(1)
        try:
            res = self.driver.find_element_by_xpath('//*[@id="doc-main"]/div/div/div/div/div[6]/p').text
        except:
            res = '没有获取成功'
        self.driver.quit()
        return res

    def apply_succee(self,phone):
        '''申请成功'''
        self.driver.find_element_by_xpath('//button[@ng-click="goSchoolApply()"]').click() # 待处理
        time.sleep(1.5)
        self.driver.find_element_by_xpath('//*[@id="formAction"]/p[2]/input').send_keys(phone) # 输入手机号
        time.sleep(0.3)
        self.driver.find_element_by_xpath('//*[@id="formAction"]/button').click() # 点击搜索
        time.sleep(1)
        self.driver.find_element_by_xpath('//*[@id="doc-main"]/div/div/div[2]/table/tbody/tr/td[1]/p').click() # 点击搜索的学校
        time.sleep(1)
        self.driver.find_element_by_xpath('//*[@id="doc-main"]/div/div/div/div[2]/div[2]/div[1]/div[2]/div[2]/div[1]/label/input').click() # 点击创建新学校
        time.sleep(0.3)
        self.driver.find_element_by_xpath('//*[@id="doc-main"]/div/div/div/div[2]/div[3]/button[1]').click() # 点击确定
        time.sleep(2)
        self.driver.quit()

    def refuse_application(self):
        '''拒绝申请'''
        self.driver = webdriver.Chrome()
        self.driver.get('http://dev.managerebuild.vanthink.cn/index/login')
        self.driver.find_element_by_id('v_username').send_keys('13511111111')
        self.driver.find_element_by_id('v_passwd').send_keys('123123')
        self.driver.find_element_by_id('v_login').click()
        time.sleep(5)
        self.driver.find_element_by_xpath('/html/body/div[2]/ul/li[2]/a').click()
        time.sleep(1)
        self.driver.find_element_by_xpath('/html/body/div[2]/ul/li[2]/ul/li[1]/a').click()
        time.sleep(2)
        self.driver.find_element_by_xpath('//*[@id="doc-main"]/div/div/div[1]/div[2]/div[1]/button').click()
        time.sleep(2)
        info_ele = self.driver.find_element_by_xpath('//*[@id="doc-main"]/div/div/div[2]/table/tbody/tr[1]/td[1]/p')
        if info_ele.text == 'x-x-h高级中学':
            info_ele.click()
            time.sleep(1.5)
            self.driver.find_element_by_xpath('//*[@id="doc-main"]/div/div/div/div[2]/div[3]/button[2]').click()
            time.sleep(2)
            self.driver.find_element_by_xpath('/html/body/div[6]/div[3]/button[1]').click()
            time.sleep(2)
            print('✅审批结束。。。拒绝')
        self.driver.quit()

    def del_school(self,schoolName='xxh高级中学'):
        self.driver.find_element_by_id('schoolName').send_keys(schoolName)
        time.sleep(0.5)
        self.driver.find_element_by_xpath('//li[@class="ui-menu-item"]').click()
        time.sleep(0.3)
        self.driver.find_element_by_xpath('//*[@id="formAction"]/button').click()
        time.sleep(0.5)
        self.driver.find_element_by_xpath('//*[@id="doc-main"]/div/div/div[3]/div[3]/table/tbody/tr/th[2]').click() # 点击第一条数据
        time.sleep(1)
        self.driver.find_element_by_xpath('//*[@id="doc-main"]/div/div/div[2]/h4/img').click() # 对学校信息进行编辑
        time.sleep(1)
        js = "var q=document.documentElement.scrollTop=100000"
        self.driver.execute_script(js)
        time.sleep(3)
        self.driver.find_element_by_xpath('//*[@id="doc-main"]/div/div/div[2]/div/div[2]/div[3]/button[1]').click() # 点击校长
        time.sleep(0.5)
        self.driver.find_element_by_xpath('//*[@id="doc-main"]/div/div/div[5]/div/div/div[2]/div[5]/button[2]').click()
        time.sleep(0.5)
        self.driver.find_element_by_xpath('//*[@id="doc-main"]/div/div/div[5]/div/div/div[2]/div[5]/button[2]').click() # 点击 确定
        time.sleep(0.5)
        self.driver.find_element_by_xpath('//*[@id="doc-main"]/div/div/div[2]/div/div[2]/div[3]/button[2]').click()
        time.sleep(0.5)
        print('✅学校删除成功！！！')
        self.driver.quit()


if __name__ == '__main__':
    '''
    department ： {'管理组':'proinfo','市场部':'market','教研组':'teaching','运维部':'operate','财务组':'finance'}
    opr_type ： {'proinfo:{'数据总览':1,'趋势图':2,'员工与权限':3,'员工申请':4,'登陆轨迹':5,}}
                {'market:{'待处理':1,'概况':2,'学校管理':3,'用户管理':4,'验证码查询':5,'词霸天看板':6}}
                {'teaching:{'题库管理':1,'词库管理':2,'听力等级管理':3,'标签管理':4,'ES管理':5,'题源管理':6,'发音修补':7,'老师首页推荐':8}}
                {'operate:{'抽奖卡片':1,'游戏管理':2,'学校管理':3,'版本管理':4,'banner管理':5}}
                {'finance:{'常用操作':1,'学校往来':2}}
    '''
    # web_driver = OprWeb(type={'department':'market','opr_type':5},phone='18955555555',code=('school','bind'))
    web_driver = OprWeb(type={'department':'market','opr_type':3})
    web_driver.management_login()
    res = web_driver.del_school()
