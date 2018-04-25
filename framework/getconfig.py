#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/4/24 11:28
# @Author  : StalloneYang
# @File    : getconfig.py
# @desc:获取基础数据
import configparser  # ---3.6的库
import os.path
from framework.logger import Logger

# create a logger instance
logger = Logger(logger="GetInfo").getlog()


class GetConfig(object):
    # config = ConfigParser.ConfigParser()
    config = configparser.ConfigParser()
    # file_path = os.path.dirname(os.getcwd()) + '/config/config.ini'
    file_path = os.path.dirname(os.path.abspath('.')) + '/config/config.ini'
    # config.read(file_path)
    config.read(file_path, encoding="utf-8-sig")

    u'''####浏览器和测试地址的选择###'''
    browser = config.get("browserType", "browserName")
    url = config.get("loginName", "URL")
    testname = config.get("loginName", "testName")

    u'''#########登录的账号#######'''
    yz_loginname = config.get("loginName", "yz_loginName")
    jl_loginname = config.get("loginName", "jl_loginName")
    sgzb_loginname = config.get("loginName", "sgzb_loginName")
    sgfb_loginname = config.get("loginName", "sgfb_loginName")
    sgzb2_loginname = config.get("loginName", "sgzb2_loginName")
    sgfb2_loginname = config.get("loginName", "sgfb2_loginName")
    sgjfb_loginname = config.get("loginName", "sgjfb_loginName")
    sjzb_loginname = config.get("loginName", "sjzb_loginName")
    sjfb_loginname = config.get("loginName", "sjfb_loginName")
    kc_loginname = config.get("loginName", "kc_loginName")

    u'''#########业主#######'''
    yz_projectName = config.get("loginName", "yz_projectName")
    yz_compKeyword = config.get("loginName", "yz_compKeyword")
    yz_compName = config.get("loginName", "yz_compName")
    yz_name = config.get("loginName", "yz_name")
    yz_nameID = config.get("loginName", "yz_nameID")

    u'''#########监理#######'''
    jl_projectName = config.get("loginName", "jl_projectName")
    jl_compKeyword = config.get("loginName", "jl_compKeyword")
    jl_compName = config.get("loginName", "jl_compName")
    jl_name = config.get("loginName", "jl_name")
    jl_nameID = config.get("loginName", "jl_nameID")

    u'''#########施工总包#######'''
    sgzb_projectName = config.get("loginName", "sgzb_projectName")
    sgzb_compKeyword = config.get("loginName", "sgzb_compKeyword")
    sgzb_compName = config.get("loginName", "sgzb_compName")
    sgzb_name = config.get("loginName", "sgzb_name")
    sgzb_nameID = config.get("loginName", "sgzb_nameID")

    u'''#########施工分包#######'''
    sgfb_projectName = config.get("loginName", "sgfb_projectName")
    sgfb_compKeyword = config.get("loginName", "sgfb_compKeyword")
    sgfb_compName = config.get("loginName", "sgfb_compName")
    sgfb_name = config.get("loginName", "sgfb_name")
    sgfb_nameID = config.get("loginName", "sgfb_nameID")

    u'''#########施工总包2#######'''
    sgzb2_projectName = config.get("loginName", "sgzb2_projectName")
    sgzb2_compKeyword = config.get("loginName", "sgzb2_compKeyword")
    sgzb2_compName = config.get("loginName", "sgzb2_compName")
    sgzb2_name = config.get("loginName", "sgzb2_name")
    sgzb2_nameID = config.get("loginName", "sgzb2_nameID")

    u'''#########施工分包2#######'''
    sgfb2_projectName = config.get("loginName", "sgfb2_projectName")
    sgfb2_compKeyword = config.get("loginName", "sgfb2_compKeyword")
    sgfb2_compName = config.get("loginName", "sgfb2_compName")
    sgfb2_name = config.get("loginName", "sgfb2_nameID")
    sgfb2_nameID = config.get("loginName", "sgfb2_nameID")

    u'''#########施工甲分包#######'''
    sgjfb_projectName = config.get("loginName", "sgjfb_projectName")
    sgjfb_compKeyword = config.get("loginName", "sgjfb_compKeyword")
    sgjfb_compName = config.get("loginName", "sgjfb_compName")
    sgjfb_name = config.get("loginName", "sgjfb_name")
    sgjfb_nameID = config.get("loginName", "sgjfb_nameID")

    u'''#########设计总包#######'''
    sjzb_projectName = config.get("loginName", "sjzb_projectName")
    sjzb_compKeyword = config.get("loginName", "sjzb_compKeyword")
    sjzb_compName = config.get("loginName", "sjzb_compName")
    sjzb_name = config.get("loginName", "sjzb_name")
    sjzb_nameID = config.get("loginName", "sjzb_nameID")

    u'''#########设计分包#######'''
    sjfb_projectName = config.get("loginName", "sjfb_projectName")
    sjfb_compKeyword = config.get("loginName", "sjfb_compKeyword")
    sjfb_compName = config.get("loginName", "sjfb_compName")
    sjfb_name = config.get("loginName", "sjfb_name")
    sjfb_nameID = config.get("loginName", "sjfb_nameID")

    u'''#########勘察#######'''
    kc_projectName = config.get("loginName", "kc_projectName")
    kc_compKeyword = config.get("loginName", "kc_compKeyword")
    kc_compName = config.get("loginName", "kc_compName")
    kc_name = config.get("loginName", "kc_name")
    kc_nameID = config.get("loginName", "kc_nameID")

    def get_browser(self):
        u"""选择浏览器"""
        # logger.info("You had select %s browser." % self.browser)
        return self.browser

    def get_url(self):
        u'''测试地址URL'''
        # logger.info("The test server url1 is: %s" % self.url1)
        return self.url

    def get_testname(self):
        u'''测试地址URL'''
        logger.info("The test server url1 is: %s" % self.testname)
        return self.testname

    # 获取登录的账号，返回 13700000000
    def get_loginName(self, get_loginName):
        u""" 登录的账号 如业主：“13700000000”或者“yz”"""

        if get_loginName == "yz_loginName" or get_loginName == "yz" or get_loginName == 13700000000:  # 业主
            logger.info("The test loginname  is: 业主 %s" % self.yz_loginname)  # yz_loginname
            return self.yz_loginname
        elif get_loginName == "jl_loginName" or get_loginName == "jl" or get_loginName == 13711111111:  # 监理
            logger.info("The test loginname  is: 监理 %s" % self.jl_loginname)
            return self.jl_loginname
        elif get_loginName == "sgzb_loginName" or get_loginName == "sgzb" or get_loginName == 13722222222:  # 施工总包
            logger.info("The test loginname  is: 施工总包 %s" % self.sgzb_loginname)
            return self.sgzb_loginname
        elif get_loginName == "sgfb_loginName" or get_loginName == "sgfb" or get_loginName == 13755555555:  # 施工分包
            logger.info("The test loginname  is: 施工分包 %s" % self.sgfb_loginname)
            return self.sgfb_loginname
        elif get_loginName == "sgzb2_loginName" or get_loginName == "sgzb2" or get_loginName == 13733333333:  # 施工总包2
            logger.info("The test loginname  is: 施工总包2 %s" % self.sgzb2_loginname)
            return self.sgzb2_loginname
        elif get_loginName == "sgfb2_loginName" or get_loginName == "sgfb2" or get_loginName == 13744444444:  # 施工分包2
            logger.info("The test loginname  is: 施工分包2 %s" % self.sgfb2_loginname)
            return self.sgfb2_loginname
        elif get_loginName == "sgjfb_loginName" or get_loginName == "sgjfb" or get_loginName == 13766666666:  # 施工甲分包
            logger.info("The test loginname  is: 施工甲分包 %s" % self.sgjfb_loginname)
            return self.sgjfb_loginname
        elif get_loginName == "sjzb_loginName" or get_loginName == "sjzb" or get_loginName == 1377777777:  # 设计总包
            logger.info("The test loginname  is: 设计总包 %s" % self.sjzb_loginname)
            return self.sjzb_loginname
        elif get_loginName == "sjfb_loginName" or get_loginName == "sjfb" or get_loginName == 13788888888:  # 设计分包
            logger.info("The test loginname  is: 设计分包 %s" % self.sjfb_loginname)
            return self.sjfb_loginname
        elif get_loginName == "kc_loginName" or get_loginName == "kc" or get_loginName == 13799999999:  # 勘察
            logger.info("The test loginname  is: 勘察 %s" % self.kc_loginname)
            return self.kc_loginname

    # 获取登录的项目名称，返回 业主深圳湾生态科技园02
    def get_projectName(self, type):
        u""" 登录的账号项目名称 ：业主深圳湾生态科技园02"""

        if type == "yz_projectName" or type == "yz" or type == 13700000000:  # 业主
            logger.info("The test projectName  is:  %s" % self.yz_projectName)  # yz_loginname
            return self.yz_projectName
        elif type == "jl_projectName" or type == "jl" or type == 13711111111:  # 监理
            logger.info("The test projectName  is:  %s" % self.jl_projectName)
            return self.jl_projectName
        elif type == "sgzb_projectName" or type == "sgzb" or type == 13722222222:  # 施工总包
            logger.info("The test projectName  is:  %s" % self.sgzb_projectName)
            return self.sgzb_projectName
        elif type == "sgfb_projectName" or type == "sgfb" or type == 13755555555:  # 施工分包
            logger.info("The test projectName  is:  %s" % self.sgfb_projectName)
            return self.sgfb_projectName
        elif type == "sgzb2_projectName" or type == "sgzb2" or type == 13733333333:  # 施工总包2
            logger.info("The test projectName  is:  %s" % self.sgzb2_projectName)
            return self.sgzb2_projectName
        elif type == "sgfb2_projectName" or type == "sgfb2" or type == 13744444444:  # 施工分包2
            logger.info("The test projectName  is:  %s" % self.sgfb2_projectName)
            return self.sgfb2_projectName
        elif type == "sgjfb_projectName" or type == "sgjfb" or type == 13766666666:  # 施工甲分包
            logger.info("The test projectName  is:  %s" % self.sgjfb_projectName)
            return self.sgjfb_projectName
        elif type == "sjzb_projectName" or type == "sjzb" or type == 1377777777:  # 设计总包
            logger.info("The test projectName  is:  %s" % self.sjzb_projectName)
            return self.sjzb_projectName
        elif type == "sjfb_projectName" or type == "sjfb" or type == 13788888888:  # 设计分包
            logger.info("The test projectName  is:  %s" % self.sjfb_projectName)
            return self.sjfb_projectName
        elif type == "kc_projectName" or type == "kc" or type == 13799999999:  # 勘察
            logger.info("The test projectName  is:  %s" % self.kc_projectName)
            return self.kc_projectName

            # 获取登录的项目名称，返回 业主深圳湾生态科技园02

    def get_name(self, type):
        u""" 登录的账号项目名称 ：业主深圳湾生态科技园02"""

        if type == "yz_name" or type == "yz" or type == 13700000000:  # 业主
            logger.info("The test projectName  is:  %s" % self.yz_name)  # yz_loginname
            return self.yz_name
        elif type == "jl_name" or type == "jl" or type == 13711111111:  # 监理
            logger.info("The test projectName  is:  %s" % self.jl_name)
            return self.jl_name
        elif type == "sgzb_name" or type == "sgzb" or type == 13722222222:  # 施工总包
            logger.info("The test projectName  is:  %s" % self.sgzb_name)
            return self.sgzb_name
        elif type == "sgfb_name" or type == "sgfb" or type == 13755555555:  # 施工分包
            logger.info("The test projectName  is:  %s" % self.sgfb_name)
            return self.sgfb_name
        elif type == "sgzb2_name" or type == "sgzb2" or type == 13733333333:  # 施工总包2
            logger.info("The test projectName  is:  %s" % self.sgzb2_name)
            return self.sgzb2_name
        elif type == "sgfb2_name" or type == "sgfb2" or type == 13744444444:  # 施工分包2
            logger.info("The test projectName  is:  %s" % self.sgfb2_name)
            return self.sgfb2_name
        elif type == "sgjfb_name" or type == "sgjfb" or type == 13766666666:  # 施工甲分包
            logger.info("The test projectName  is:  %s" % self.sgjfb_name)
            return self.sgjfb_name
        elif type == "sjzb_name" or type == "sjzb" or type == 1377777777:  # 设计总包
            logger.info("The test projectName  is:  %s" % self.sjzb_name)
            return self.sjzb_name
        elif type == "sjfb_name" or type == "sjfb" or type == 13788888888:  # 设计分包
            logger.info("The test projectName  is:  %s" % self.sjfb_name)
            return self.sjfb_name
        elif type == "kc_name" or type == "kc" or type == 13799999999:  # 勘察
            logger.info("The test projectName  is:  %s" % self.kc_name)
            return self.kc_name

    def get_yz_info(self, get_info):
        u'''获取业主数据'''

        if get_info == "yz_compKeyword":
            logger.info("业主公司关键词是： %s" % self.yz_compKeyword)
            return self.yz_compKeyword
        elif get_info == "yz_loginName":
            logger.info("The test loginname  is: 业主 %s" % self.yz_loginname)
            return self.yz_loginname
        elif get_info == "yz_compName":
            logger.info("业主的公司名称是： %s" % self.yz_compName)
            return self.yz_compName
        elif get_info == "yz_name":
            logger.info("业主名字是： %s" % self.yz_name)
            return self.yz_name
        elif get_info == "yz_nameID":
            logger.info("业主账号ID是： %s" % self.yz_nameID)
            return self.yz_nameID
        elif get_info == "yz_projectName":
            logger.info("业主项目名称是： %s" % self.yz_projectName)
            return self.yz_projectName

    def get_jl_info(self, get_info):
        u'''获取监理数据'''

        if get_info == "jl_compKeyword":
            logger.info(u"监理公司关键词是： %s" % self.jl_compKeyword)
            return self.jl_compKeyword
        elif get_info == "jl_loginName":
            logger.info("The test loginname  is: 监理 %s" % self.jl_loginname)
            return self.jl_loginname
        elif get_info == "jl_compName":
            logger.info("监理的公司名称是： %s" % self.jl_compName)
            return self.jl_compName
        elif get_info == "jl_name":
            logger.info("监理名字是： %s" % self.jl_name)
            return self.jl_name
        elif get_info == "jl_nameID":
            logger.info("监理账号ID是： %s" % self.jl_nameID)
            return self.jl_nameID
        elif get_info == "jl_projectName":
            logger.info("监理项目名称是： %s" % self.jl_projectName)
            return self.jl_projectName

    def get_sgzb_info(self, get_info):
        u'''获取施工总包数据'''

        if get_info == "sgzb_compKeyword":
            logger.info("施工总包公司关键词是： %s" % self.sgzb_compKeyword)
            return self.sgzb_compKeyword
        elif get_info == "sgzb_loginName":
            logger.info("The test loginname  is: 施工总包 %s" % self.sgzb_loginname)
            return self.sgzb_loginname
        elif get_info == "sgzb_compName":
            logger.info("施工总包的公司名称是： %s" % self.sgzb_compName)
            return self.sgzb_compName
        elif get_info == "sgzb_name":
            logger.info("施工总包名字是： %s" % self.sgzb_name)
            return self.sgzb_name
        elif get_info == "sgzb_nameID":
            logger.info("施工总包账号ID是： %s" % self.sgzb_nameID)
            return self.sgzb_nameID
        elif get_info == "sgzb_projectName":
            logger.info("施工总包项目名称是： %s" % self.sgzb_projectName)
            return self.sgzb_projectName

    def get_sgfb_info(self, get_info):
        u'''获取施工分包数据'''

        if get_info == "sgfb_compKeyword":
            logger.info("施工分包公司关键词是： %s" % self.sgfb_compKeyword)
            return self.sgfb_compKeyword
        elif get_info == "sgfb_loginName":
            logger.info("The test loginname  is: 施工分包 %s" % self.sgfb_loginname)
            return self.sgfb_loginname
        elif get_info == "sgfb_compName":
            logger.info("施工分包的公司名称是： %s" % self.sgfb_compName)
            return self.sgfb_compName
        elif get_info == "sgfb_name":
            logger.info("施工分包名字是： %s" % self.sgfb_name)
            return self.sgfb_name
        elif get_info == "sgfb_nameID":
            logger.info("施工分包账号ID是： %s" % self.sgfb_nameID)
            return self.sgfb_nameID
        elif get_info == "sgfb_projectName":
            logger.info("施工分包项目名称是： %s" % self.sgfb_projectName)
            return self.sgfb_projectName

    def get_sgzb2_info(self, get_info):
        u'''获取施工总包2数据'''

        if get_info == "sgzb2_compKeyword":
            logger.info("施工总包2公司关键词是： %s" % self.sgzb2_compKeyword)
            return self.sgzb2_compKeyword
        elif get_info == "sgzb2_loginName":
            logger.info("The test loginname  is: 施工总包2 %s" % self.sgzb2_loginname)
            return self.sgzb2_loginname
        elif get_info == "sgzb2_compName":
            logger.info("施工总包2的公司名称是： %s" % self.sgzb2_compName)
            return self.sgzb2_compName
        elif get_info == "sgzb2_name":
            logger.info("施工总包2名字是： %s" % self.sgzb2_name)
            return self.sgzb2_name
        elif get_info == "sgzb2_nameID":
            logger.info("施工总包2账号ID是： %s" % self.sgzb2_nameID)
            return self.sgzb2_nameID
        elif get_info == "sgzb2_projectName":
            logger.info("施工总包2项目名称是： %s" % self.sgzb2_projectName)
            return self.sgzb2_projectName

    def get_sgfb2_info(self, get_info):
        u'''获取施工分包2数据'''

        if get_info == "sgfb2_compKeyword":
            logger.info("施工分包2公司关键词是： %s" % self.sgfb2_compKeyword)
            return self.sgfb2_compKeyword
        elif get_info == "sgfb2_loginName":
            logger.info("The test loginname  is: 施工分包2 %s" % self.sgfb2_loginname)
            return self.sgfb2_loginname
        elif get_info == "sgfb2_compName":
            logger.info("施工分包2的公司名称是： %s" % self.sgfb2_compName)
            return self.sgfb2_compName
        elif get_info == "sgfb2_name":
            logger.info("施工分包2名字是： %s" % self.sgfb2_name)
            return self.sgfb2_name
        elif get_info == "sgfb2_nameID":
            logger.info("施工分包2账号ID是： %s" % self.sgfb2_nameID)
            return self.sgfb2_nameID
        elif get_info == "sgfb2_projectName":
            logger.info("施工分包2项目名称是： %s" % self.sgfb2_projectName)
            return self.sgfb2_projectName

    def get_sgjfb_info(self, get_info):
        u'''获取施工甲分包数据'''

        if get_info == "sgjfb_compKeyword":
            logger.info("施工甲分包公司关键词是： %s" % self.sgjfb_compKeyword)
            return self.sgjfb_compKeyword
        elif get_info == "sgjfb_loginName":
            logger.info("The test loginname  is: 施工甲分包 %s" % self.sgjfb_loginname)
            return self.sgjfb_loginname
        elif get_info == "sgjfb_compName":
            logger.info("施工甲分包的公司名称是： %s" % self.sgjfb_compName)
            return self.sgjfb_compName
        elif get_info == "sgjfb_name":
            logger.info("施工甲分包名字是： %s" % self.sgjfb_name)
            return self.sgjfb_name
        elif get_info == "sgjfb_nameID":
            logger.info("施工甲分包账号ID是： %s" % self.sgjfb_nameID)
            return self.sgjfb_nameID
        elif get_info == "sgjfb_projectName":
            logger.info("施工甲分包项目名称是： %s" % self.sgjfb_projectName)
            return self.sgjfb_projectName

    def get_sjzb_info(self, get_info):
        u'''获取设计总包数据'''

        if get_info == "sjzb_compKeyword":
            logger.info("设计总包公司关键词是： %s" % self.sjzb_compKeyword)
            return self.sjzb_compKeyword
        elif get_info == "sjzb_loginName":
            logger.info("The test loginname  is: 设计总包 %s" % self.sjzb_loginname)
            return self.sjzb_loginname
        elif get_info == "sjzb_compName":
            logger.info("设计总包的公司名称是： %s" % self.sjzb_compName)
            return self.sjzb_compName
        elif get_info == "sjzb_name":
            logger.info("设计总包名字是： %s" % self.sjzb_name)
            return self.sjzb_name
        elif get_info == "sjzb_nameID":
            logger.info("设计总包账号ID是： %s" % self.sjzb_nameID)
            return self.sjzb_nameID
        elif get_info == "sjzb_projectName":
            logger.info("设计总包项目名称是： %s" % self.sjzb_projectName)
            return self.sjzb_projectName

    def get_sjfb_info(self, get_info):
        u'''获取设计分包数据'''

        if get_info == "sjfb_compKeyword":
            logger.info("设计分包公司关键词是： %s" % self.sjfb_compKeyword)
            return self.sjfb_compKeyword
        elif get_info == "sjfb_loginName":
            logger.info("The test loginname  is: 设计分包 %s" % self.sjfb_loginname)
            return self.sjfb_loginname
        elif get_info == "sjfb_compName":
            logger.info("设计分包的公司名称是： %s" % self.sjfb_compName)
            return self.sjfb_compName
        elif get_info == "sjzb_name":
            logger.info("设计分包名字是： %s" % self.sjfb_name)
            return self.sjfb_name
        elif get_info == "sjfb_nameID":
            logger.info("设计分包账号ID是： %s" % self.sjfb_nameID)
            return self.sjfb_nameID
        elif get_info == "sjfb_projectName":
            logger.info("设计分包项目名称是： %s" % self.sjfb_projectName)
            return self.sjfb_projectName

    def get_kc_info(self, get_info):
        u'''获取勘察数据'''

        if get_info == "kc_compKeyword":
            logger.info("勘察公司关键词是： %s" % self.kc_compKeyword)
            return self.kc_compKeyword
        elif get_info == "kc_loginName":
            logger.info("The test loginname  is: 勘察 %s" % self.kc_loginname)
            return self.kc_loginname
        elif get_info == "kc_compName":
            logger.info("勘察的公司名称是： %s" % self.kc_compName)
            return self.kc_compName
        elif get_info == "kc_name":
            logger.info("勘察名字是： %s" % self.kc_name)
            return self.kc_name
        elif get_info == "kc_nameID":
            logger.info("勘察账号ID是： %s" % self.kc_nameID)
            return self.kc_nameID
        elif get_info == "kc_projectName":
            logger.info("勘察项目名称是： %s" % self.kc_projectName)
            return self.kc_projectName


if __name__ == "__main__":
    print("nihao a ")

