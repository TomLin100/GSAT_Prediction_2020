# -*- coding: utf-8 -*-
"""
Created on Sat Feb 15 03:55:55 2020

@author: jialing
"""

import pandas as pd
import Tool
def merge():
    gr_df = pd.DataFrame(pd.read_csv('OutputGSAT.csv',dtype ='str'))
    citypp_df = pd.DataFrame(pd.read_csv('OutputGrVsCityPP.csv',dtype ='str'))
    dd_df = pd.DataFrame(pd.read_csv('OutputGrVsDurl.csv',dtype ='str'))
    salary_df = pd.DataFrame(pd.read_csv('OutputGrVsSalary.csv',dtype ='str'))
    ud_df = pd.DataFrame(pd.read_csv('OutputGrVsUurl.csv',dtype ='str'))
    
    for x in range(len(gr_df)):
        for y1 in range(len(citypp_df)):
            if gr_df['DID'][x]==citypp_df['DID'][y1]:
                gr_df['City'][x]=citypp_df['City'][y1]
                gr_df['PP'][x]=citypp_df['PP'][y1]
        for y2 in range(len(dd_df)):
            if gr_df['DID'][x]==dd_df['DID'][y2]:
                gr_df['DURL'][x]=dd_df['DURL'][y2]
        for y3 in range(len(salary_df)):
            if gr_df['DID'][x]==salary_df['DID'][y3]:
                gr_df['Salary'][x]=salary_df['Salary'][y3]
                gr_df['SalaryURL'][x]=salary_df['SalaryURL'][y3]
        for y4 in range(len(ud_df)):
            if gr_df['DID'][x]==ud_df['DID'][y4]:
                gr_df['UURL'][x]=ud_df['UURL'][y4]
    
    gr_df.to_csv("D.csv", encoding="utf_8_sig",index=False)
    Tool.SaveDatabase(gr_df,"D")
