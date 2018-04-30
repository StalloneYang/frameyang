#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/4/25 14:53
# @Author  : StalloneYang
# @File    : runAllCase.py
# @desc:运行所有测试脚本

from framework.BeautifulReport.BeautifulReport import BeautifulReport # 新报告样式，需导入BeautifulReport
from framework import HTMLTestRunner
import os
import unittest
import time
from framework.SendEmail import SendMail

# 设置报告文件保存路径
# 当前文件的路径
curpath = os.path.dirname(os.path.realpath(__file__))
# 当前文件的父路径
father_path=os.path.abspath(os.path.dirname(curpath)+os.path.sep+".")
# 报告路径
report_path = os.path.join(father_path, "reports")
# 获取系统当前时间
now = time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime(time.time()))

casepath = os.path.join(father_path, "cases")

# 构建suite
allCase = unittest.defaultTestLoader.discover(casepath,pattern="test*.py")
# allCase = unittest.defaultTestLoader.discover(r"E:\workspace\frameyang\cases", "test*.py")
print("打印执行的测试套件：%s" % allCase)


if __name__ =='__main__':
    # # 设置报告名称格式
    # HtmlFile = report_path + "\\智慧工程2.0测试报告" + now + ".html"
    # fp = open(HtmlFile, "wb")
    # # 初始化一个HTMLTestRunner实例对象，用来生成报告
    # runner = HTMLTestRunner.HTMLTestRunner(stream=fp, verbosity=2, title=u"智慧工程2.0自动化测试报告", description=u"用例测试情况")
    # # 开始执行测试套件
    # runner.run(allCase)
    # fp.close()

    # 用新样式生成测试报告,    BeautifulReport需去Git，放在site-packages的下面
    HtmlFile = report_path
    result = BeautifulReport(allCase)  # 最新的报告样式
    result.report(filename='智慧工程2.0测试报告%s'%now, description='执行所有智慧工程2.0的测试用例', log_path=HtmlFile)

    # 测试结束之后，执行邮件发送报告
    sendMail = SendMail()
    sendMail.send()






