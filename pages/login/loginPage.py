#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/4/24 11:33
# @Author  : StalloneYang
# @File    : loginPage.py
# @desc: 登录页面

from framework.base import BasePage
from framework.getconfig import GetConfig
from framework.logger import Logger

logger = Logger(logger="LoginPage").getlog()
getconfig = GetConfig()

class LoginPage(BasePage):
    def __init__(self, driver):
        self.driver = driver
        self.loginbtn_first = "xpath=>//a[contains(.,'登录')]"  # 首页左上角的登录按钮(只适用于chrome浏览器)
        self.username_org = "css=>input.login-text"  # 项目用户名输入框
        self.username_ent = "xpath=>(//input[@type='text'])[2]"  # 企业用户名输入框
        self.password_org = "xpath=>//input[@type='password']"  # 项目密码输入框
        self.password_ent = "xpath=>(//input[@type='password'])[2]"  # 企业密码输入框
        # self.loginbtn_first = "l=>登录"  # 首页左上角的登录按钮(只适用于chrome浏览器)
        self.loginbtn_org = "xpath=>//input[contains(@systype,'1')]"  # 项目登录按钮
        self.loginbtn_ent = "xpath=>(//input[@value='登录'])[2]"  # 企业登录按钮
        self.select_orgbtn = "xpath=>//li[contains(.,'项目人员登录')]"  # 切换项目登录按钮
        self.select_entbtn = "xpath=>//li[contains(.,'企业管理员登录')]"  # 切换企业登录按钮
        self.name = "xpath=>//span[@data-reactid='.0.$0/=10.0.0.1.0.0.1.0.1']"  # 登录成功后的用户名
        self.curryproject = "xpath=>//span[@class='show fw-700 ellipsis']"  # 项目名称
        self.switch_projectname_btn = "xpath=>//div[@class='companyDown pointer']"  # 切换项目的按钮
        self.logout = "xpath=>//i[@class='ids guanbituichu']"

    def get_name(self):
        '''获取登录成功后的名字'''
        name = self.text(self.name)
        logger.info("账号登录成功的名字是：%s !" % name)
        return name

    def input_username_org(self, text):
        self.input_text(self.username_org, text)
        logger.info("输入项目账号：" + text)

    def input_username_ent(self, text):
        self.input_text(self.username_ent, text)
        logger.info("输入企业账号：" + text)

    def input_password_org(self, text):
        self.input_text(self.password_org, text)
        logger.info("输入项目账号密码：" + text)

    def input_password_ent(self, text):
        self.input_text(self.password_ent, text)
        logger.info("输入企业账号的密码：" + text)

    # 点击首页左上角的登录按钮
    def click_loginbtn_first(self):
        u"""点击首页左上角的登录按钮"""
        self.click(self.loginbtn_first)
        logger.info("点击首页左上角的登录按钮")

    # 点击到项目登录按钮
    def click_loginbtn_org(self):
        u"""点击项目登录按钮"""
        self.click(self.loginbtn_org)
        logger.info("点击项目登录按钮")

    # 点击切换到企业登录按钮
    def click_loginbtn_ent(self):
        u"""点击企业登录按钮"""
        self.click(self.loginbtn_ent)
        logger.info("点击到企业登录按钮")

    # 点击退出按钮
    def click_logoutbtn(self):
        u"""点击退出按钮"""
        self.click(self.logout)
        logger.info("点击退出按钮")

    # 点击切换项目登录按钮
    def select_org_loginbtn(self):
        u"""点击切换项目登录按钮"""
        self.click(self.select_orgbtn)
        logger.info("点击切换项目登录按钮")

    # 点击切换企业登录按钮
    def select_ent_loginbtn(self):
        u"""点击切换企业登录按钮"""
        self.click(self.select_entbtn)
        logger.info("点击切换企业登录按钮")

    # 项目登录
    def login_org(self, loginName):
        u'''项目登录'''
        self.click_loginbtn_first()
        # loginname = self.select_access(loginName)   #判断什么类型账号登录
        loginname = getconfig.get_loginName(loginName)  # 判断什么类型账号登录
        self.input_username_org(loginname)
        self.input_password_org("88888888")
        self.click_loginbtn_org()
        # self.switch_project(loginName)

    # 企业登录
    def login_ent(self, loginName):
        u"""企业登录"""
        self.click_loginbtn_first()
        loginname = getconfig.get_loginName(loginName)  # 判断什么类型账号登录
        self.select_ent_loginbtn()
        self.input_username_ent(loginname)
        self.input_password_ent("88888888")
        self.click_loginbtn_ent()
        self.sleep(2)

    # 获取config的项目登录成功的工程名称或项目名称
    def get_project_name_config(self):
        u'''获取登录成功的工程名称或项目名称'''
        _ye_project_Name = getconfig.get_yz_info("yz_projectName")
        return _ye_project_Name

    # 切换项目
    def switch_project(self, type):
        u'''切换项目'''
        co_projectname = self.get_project_name_config()  # 获取配置文件的项目名称
        # self.sleep(1)
        cu_projectname = self.get_text(self.curryproject)  # 获取当前登录成功的项目名称
        if cu_projectname == co_projectname:
            logger.info(u"不用切换项目!")
            # self.sleep(1)  # 太快了，定位不到菜单，直接悬浮切换项目按钮了   也有可能是项目名字三个字
        else:
            self.museover(self.switch_projectname_btn)
            _projectName = getconfig.get_projectName(type)
            # driver.find_element_by_xpath(u"//li[@title='深圳平安大厦']").click()
            select_curryproject = "xpath=>//li[@title='" + _projectName + "']"  # 点击选择当前测试项目
            self.focus2(select_curryproject)
            self.click(select_curryproject)



