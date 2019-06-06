import os,re,json,subprocess

class Utils:
    _con = {
        'capabilities':
            [
                {
                    'browserName': 'Chrome',
                    'platformVersion': '28',
                    'maxInstances': 1,
                    'platformName': 'Android',
                    'automationName': 'UiAutomator2',
                    'deviceName': '6'
                }
            ],
        'configuration':
            {
                'url': 'http://127.0.0.1:%s/wd/hub/',
                'host': '127.0.0.1',
                'port': '',
                'cleanUpCycle': 2000,
                'timeout': 30000,
                'proxy': 'org.openqa.grid.selenium.proxy.DefaultRemoteProxy',
                'maxSession': 1,
                'register': True,
                'registerCycle': 5000,
                'hubPort': 4444,
                'hubHost': '',
                'hubProtocol': 'http'
            }
    }

    def is_using(self,port):
        """判断端口号是否被占用"""
        # Mac OS
        cmd = "netstat -an | grep %s" % port
        if os.popen(cmd).readlines():
            return True
        else:
            return False

    def get_ports(self, count):
        """获得4723端口后一系列free port"""
        port = 4723
        port_list = []
        while True:
            if len(port_list) == count:
                break
            if not self.is_using(port) and (port not in port_list):
                port_list.append(port)
            else:
                port += 2
        return port_list

    def get_pid(self,port):
        res = os.popen('lsof -i:%s'%port).read()
        pid = re.findall('.*?node.*?(\d+)', res)
        return set(pid)

    def appium_node_info(self,hubHost,port):
        self._con['configuration']['url'] = 'http://127.0.0.1:%s/wd/hub/'%port
        self._con['configuration']['port'] = '%s'%port
        self._con['configuration']['hubHost'] = hubHost
        fp = open('./mobile.json','w')
        fp.write(json.dumps(self._con))
        fp.close()

    def start_appium(self):
        port = self.get_ports(count=1)[0]
        bp = int(port) + 1000
        hubHost = '192.168.0.102'
        self.appium_node_info(hubHost=hubHost,port=port)
        CMD = 'appium -p %s -bp %s --nodeconfig /Users/vanthink_test_ios/aa/testone/mobile.json' % (port, bp)
        print('cmd:', CMD)
        subprocess.Popen(CMD, shell=True)
        return int(port)