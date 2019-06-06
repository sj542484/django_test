import subprocess
import appscript
from appium import webdriver
import time,os,sys,json
from testfarm.test_program.conf.run_cases import RunCases
from testfarm.test_program.conf.basepage import BasePage
from testfarm.test_program.conf.case_strategy import CaseStrategy
from testfarm.test_program.conf.ports import Ports
from testfarm.test_program.utils.kill_pid import killPid

class Driver:

    def __init__(self,uuid,platformVersion,deviceName):
        self.uuid = uuid
        self.platformVersion = platformVersion
        self.deviceName = deviceName

    def remote_info(self):
        desired_caps = {
            'platformName': 'Android',
            'platformVersion': '8.0',
            'deviceName': 'honor2',
            'app': '/Users/vanthink_test_ios/aa/testone/testfarm/test_program/weixin704android1420.apk',
            'unicodeKeyboard': True,
            'resetKeyboard': True,
            'noReset': True,
            'appPackage': 'com.tencent.mm',
            'automationName': 'uiautomator2',
            'appActivity': 'com.tencent.mm.ui.LauncherUI',
            'udid': 'MKJNW18524003878'
        }
        return desired_caps

    def run_cases(self,port):
        # 等待appium服务
        time.sleep(5)
        # 收集用例
        cs = CaseStrategy()
        cases = cs.collect_cases(suite=False)
        # 连接appium服务
        addr = 'http://127.0.0.1:4723/wd/hub'
        print(addr,'========================================================')
        print(self.remote_info())
        driver = webdriver.Remote(addr,self.remote_info())
        print('===============')
        # 设置driver
        base_page = BasePage()
        base_page.set_driver(driver)
        try:
            time.sleep(5)
            print('start cases')
            run_case = RunCases(self.remote_info())
            file_name = run_case.file_name
            run_case.run(cases)
            print('end')
        except Exception as e:
            print('异常：',e)
        driver.quit()
        # kill掉node服务
        killPid().kill_pid(port)
        return file_name

if __name__ == '__main__':
    dr = Driver(
        uuid = 'MKJNW18524003878',
        platformVersion = '8。0',
        deviceName = '啦啦'
    )
    dr.run_cases(port='4723')