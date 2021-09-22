# coding:utf8
import xlrd
from common.get_logger import test_datas_path

def get_logindata1():
    rd=xlrd.open_workbook(filename=test_datas_path+"logindata.xls")
    sheet1=rd.sheet_by_name("Sheet1")
    rows=sheet1.nrows
    cols=sheet1.ncols
    list1=[]
    for col in range(cols):
        list1.append(sheet1.cell_value(0,col))
    list2=[]
    for row in range(1,rows):
        dict1={}
        for col in range(cols):
            dict1[list1[col]]=sheet1.cell_value(row,col)
        list2.append(dict1)
    return list2

def get_logindata2():
    rd = xlrd.open_workbook(filename=test_datas_path + "logindata.xls")
    sheet1 = rd.sheet_by_name("Sheet2")
    rows = sheet1.nrows
    cols = sheet1.ncols
    list1 = []
    for col in range(cols):
        list1.append(sheet1.cell_value(0, col))
    list2 = []
    for row in range(1, rows):
        dict1 = {}
        for col in range(cols):
            dict1[list1[col]] = sheet1.cell_value(row, col)
        list2.append(dict1)
    return list2

def get_numberdata1():
    rd = xlrd.open_workbook(filename=test_datas_path + "logindata.xls")
    sheet1 = rd.sheet_by_name("Sheet3")
    rows = sheet1.nrows
    cols = sheet1.ncols
    list1 = []
    for col in range(cols):
        list1.append(sheet1.cell_value(0, col))
    list2 = []
    for row in range(1, rows):
        dict1 = {}
        for col in range(cols):
            dict1[list1[col]] = sheet1.cell_value(row, col)
        list2.append(dict1)
    return list2

logindatas1=get_logindata1()
logindatas2=get_logindata2()
numberdatas1=get_numberdata1()