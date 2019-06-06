import unittest
from testfarm.test_program.app.weixin.element.public import Get_Cash
from testfarm.test_program.app.weixin.test_data.set_price import priceList
from testfarm.test_program.conf.decorator import testcase, setup, teardown

class Set_offer(unittest.TestCase):
    """团购"""
    @classmethod
    @setup
    def setUp(cls):
        """启动应用"""
        cls.public = Get_Cash()

    @classmethod
    @teardown
    def tearDown(cls):
        pass

    @testcase
    def test_offer(self):
        self.public.team_pay(priceList[-1][0])
        print('=====脚本执行完毕=====')
