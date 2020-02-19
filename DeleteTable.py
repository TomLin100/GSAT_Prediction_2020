# -*- coding: utf-8 -*-
"""
Created on Sat Feb 15 15:36:41 2020

@author: jialing
"""
import os
def deletetable():
    OutputCityPp = "OutputCityPp.csv"
    OutputDURL = "OutputDURL.csv"
    OutputGrVsClass = "OutputGrVsClass.csv"
    OutputGrVsUURL = "OutputGrVsUURL.csv"
    OutputGSAT = "OutputGSAT.csv"
    OutputSalary = "OutputSalary.csv"
    OutputSC = "OutputSC.csv"
    OutputUURL = "OutputUURL.csv"
    OutputGrVsDURL = "OutputGrVsDURL.csv"
    data = ".22各科級分人數分布表.xls"
    data2 = ".26各科成績標準一覽表.xls"
    try:
        os.remove(OutputGSAT)
        os.remove(OutputCityPp)
        os.remove(OutputSalary)
        os.remove(OutputSC)
        os.remove(OutputUURL)
        os.remove(OutputDURL)
        os.remove(OutputGrVsDURL)
        os.remove(OutputGrVsUURL)
        os.remove(OutputGrVsClass)
        os.remove(data)
        os.remove(data2)
    except OSError as e:
        print(e)
    else:
        print("File is deleted successfully")