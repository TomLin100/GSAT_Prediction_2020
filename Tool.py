# -*- coding: utf-8 -*-
"""
Created on Sat Feb 15 05:19:48 2020

@author: jialing
"""

import requests
from bs4 import BeautifulSoup
from sqlalchemy import create_engine
import pandas as pd
#存到資料庫用
from sqlalchemy.types import NVARCHAR, Float, Integer
import xlrd
import xlwt
# =============================================================================
# 訪問網站
# =============================================================================
def VisitWebsite(url):
    headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36'}
    r=requests.get(url, headers=headers)#將網頁資料GET下來
    r.encoding = 'utf-8'# 解決中文問題
    soup = BeautifulSoup(r.text,"lxml")
    return soup
# =============================================================================
# 存進資料庫
# =============================================================================
def SaveDatabase(data,Tablename):#傳入(資料表,名稱)
    engine = create_engine('mssql+pymssql://jialing:19951215@DESKTOP-FF0SSTD/GSAT_Prediction_2020?charset=utf8') 
    
    # 新建、插入操作
    try:
        data.to_sql(Tablename,engine,if_exists='replace',index=False)
#        data.to_sql(Tablename,engine,if_exists='replace',index=False,dtype = dtypedict)
        print(Tablename,"已建好")
    except Exception as e:
        print(e)

# =============================================================================
# 轉換各科成績標準一覽表(T)使用跟轉換科級分人數百分比累計表(NewScoreData)
# =============================================================================
def readExcel_T(inputFileName):
    workbook = xlrd.open_workbook(filename=inputFileName);    #讀取文件
    sheet = workbook.sheet_by_index(0);    #透過index取工作表
    #print(sheet.nrows);    #該工作表有內容的rows最大到值
    #print(sheet.ncols);    #該工作表有內容的columns最大值
    #cols = sheet.col_values(4);
    isGrade = False;
    grade = [];
    subjectCount = 0;
    i = 0;
    while i < sheet.nrows:
        for j in range(sheet.ncols):
            if str(sheet.cell(i, j).value).strip().find("級分") >= 0:
                if str(sheet.cell(i, j).value).strip().find("總級分") >= 0:
                    isGrade = False;
                else:
                    isGrade = True;
            if isGrade:
                for k in range(5):
                    grade.append(sheet.cell(i+1+k, j).value);
                subjectCount = subjectCount + 1;
                isGrade = False;
                if subjectCount == 5:
                    break;    
        if subjectCount == 5:
            break;    
        i = i + 1;
        
    return grade;

def setStyle(fontName, height, bold=False):
    style = xlwt.XFStyle();
    font = xlwt.Font();
    font.name = fontName;
    font.bold = bold;
    #font.colour_index = 3;
    font.height = height;
    style.font = font;
    return style;

def writeExcel(header, outputFileName, columns):
    file = xlwt.Workbook();
    sheet = file.add_sheet("工作表1", cell_overwrite_ok=True);
    for i in range(len(header)):
        sheet.write(0, i, header[i], setStyle("新細明體", 270, True));
    if type(columns[0]) == list:    #複數column時
        for i in range(len(columns)):
            for j in range (len(columns[i])):
                sheet.write(j + 1, i, columns[i][j], setStyle("新細明體", 270, True));
    else:    #單一column時
        for i in range(0, len(columns)):
            sheet.write(i + 1, 0, columns[i], setStyle("新細明體", 270, True));
    
    file.save(outputFileName);

def readExcel(inputFileName):
    workbook = xlrd.open_workbook(filename=inputFileName);    #讀取文件
    sheet = workbook.sheet_by_index(0);    #透過index取工作表
    #print(sheet.nrows);    #該工作表有內容的rows最大到值
    #print(sheet.ncols);    #該工作表有內容的columns最大值
    #cols = sheet.col_values(4);
    isPercentage = False;
    percentage = [];
    i = 0;
    while i < sheet.nrows:
        for j in range(sheet.ncols):
            if str(sheet.cell(i, j).value).strip().find("累計\n百分比") >= 0:
                isPercentage = True;
            if isPercentage:
                for k in range(16):
                    percentage.append(sheet.cell(i+1+k, j).value);
                    
                isPercentage = False;
                
        i = i + 1;
        
    return percentage;

def setEname(data, count, ename):
    for i in range(count):
        ename.append(data);
        
    return ename;

def setScore(count, score):
    for i in range(count, -1, -1):
        score.append(str(i));
        
    return score;