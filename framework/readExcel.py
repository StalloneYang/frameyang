#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/4/8 23:19
# @Author  : StalloneYang
# @File    : readExcel.py
# @desc: 读取Excel
import xlrd
import os

curpath = os.path.dirname(os.path.realpath(__file__))
fatherpath = os.path.abspath(os.path.dirname(curpath) + os.path.sep + ".")
filepath = os.path.join(fatherpath, "data\\test_data.xlsx")
# filepath = r"D:\Workspace\frameyang\framework\data\test_data.xlsx"

class ReadExcel(object):
    def __init__(self, excelPath=filepath, sheetName="Sheet1"):
        self.data = xlrd.open_workbook(excelPath)
        self.table = self.data.sheet_by_name(sheetName)
        # 获取第一行作为 key 值
        self.keys = self.table.row_values(0)
        # 获取总行数
        self.rowNum = self.table.nrows
        # 获取总列数
        self.colNum = self.table.ncols

    def dict_data(self):
        """返回的是一个list"""
        if self.rowNum <= 1:
            print("总行数小于 1")
        else:
            r = []
            j = 1
            for i in range(self.rowNum - 1):
                s = {}
                # 从第二行取对应 values 值
                # s['rowNum'] = i + 2  # 从Excel第二行读取
                values = self.table.row_values(j)
                for x in range(self.colNum):
                    s[self.keys[x]] = values[x]
                r.append(s)
                j += 1
            return r


if __name__ == "__main__":
    sheetName = "Sheet1"
    data = ReadExcel(filepath, sheetName)
    d = data.dict_data()
    print(type(d))
    print(data.dict_data())  # 打印Excel所有内容
    print(d[0])
    dd = d[0]
    print(type(dd))
    print(dd['id'])
    print(d[2])

