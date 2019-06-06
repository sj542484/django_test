import os
import unittest
from testfarm.test_program.conf.base_config import GetVariable as gv

class CaseStrategy:
    """测试用例搜集"""
    def _collect_cases(self, cases, top_dir=None):
        # 构造测试集  defaultTestLoader（）即TestLoader（）测试用例加载器，包括多个加载测试用例的方法，返回一个测试套件
        suites = unittest\
            .defaultTestLoader.discover(gv.CASE_PATH, pattern=gv.CASE_PATTERN, top_level_dir=top_dir)
        index = 0
        for suite in suites:
            for case in suite:
                index += 1
                print(index,' case:',case)
                cases.addTest(case)

    def collect_cases(self, suite=False):
        """collect cases
        collect cases from the giving path by case_path via the giving pattern by case_pattern
        return: all cases that collected by the giving path and pattern, it is a unittest.TestSuite()
        """
        cases = unittest.TestSuite()  # 初始化一个测试套件
        if suite:
            test_suites = []
            for file in os.listdir('.'):  # 输出所有文件和文件夹
                print(file)
                if gv.SUIT_PATH in file:
                    if os.path.isdir(file):  # 判断某一路径是否为目录
                        test_suites.append(file)  # 是目录不是文件，则append
            for test_suite in test_suites:
                self._collect_cases(cases, top_dir=test_suite)
        else:
            self._collect_cases(cases, top_dir=None)
        return cases
