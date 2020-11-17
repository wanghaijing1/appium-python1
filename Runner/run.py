# coding :utf-8
import unittest
import datetime
import os
from HTMLTestRunner import HTMLTestRunner

if __name__ == '__main__':
    suite = unittest.TestSuite()
    path = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
    report_path = path + './report/'
    if not os.path.exists(report_path):
        os.mkdir(report_path)
    else:
        pass
    now = datetime.datetime.now()
    report_name = report_path + now.strftime('%Y-%m-%d_%H-%M-%S') + '.html'
    fp = open(report_name, "wb")
    path = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
    test_dir = path + "\\testcase"
    suite.addTests(unittest.defaultTestLoader.discover(test_dir, pattern='test_*.py', top_level_dir=None))
    # HTMLTestRunner运行器
    runner = HTMLTestRunner(stream=fp, title='途家测试报告', description='用例执行情况')
    runner.run(suite)
    fp.close()
    # git 随机验证%%%%%
    fp.close()

