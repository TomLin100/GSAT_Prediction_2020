"""
Created on Sat Feb 15 15:24:06 2020

@author: jialing
"""
import pandas as pd
import Tool
import os
def oldscoredata():
    os.remove("OldScoreData.csv")
    os.rename("NewScoreData.csv","OldScoreData.csv")
    data_xls = pd.read_excel('OldScoreData.xlsx')#,encoding='utf-8'
    Tool.SaveDatabase(data_xls,"OldScoreData")