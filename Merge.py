# -*- coding: utf-8 -*-
"""
Created on Sat Feb 15 03:55:55 2020

@author: jialing
"""

import pandas as pd
import Tool
def merge():
    gr_df = pd.read_csv('OutputGSAT.csv',dtype ='str')
    citypp_df = pd.read_csv('OutputGrVsCityPP.csv',dtype ='str')
    dd_df = pd.read_csv('OutputGrVsDurl.csv',dtype ='str')
    salary_df = pd.read_csv('OutputGrVsSalary.csv',dtype ='str')
    ud_df = pd.read_csv('OutputGrVsUurl.csv',dtype ='str')
    gr_df.update(citypp_df, join='left', filter_func=None)
    gr_df.update(dd_df, join='left', filter_func=None)
    gr_df.update(salary_df, join='left', filter_func=None)
    gr_df.update(ud_df, join='left', filter_func=None)
    
    gr_df.to_csv("D.csv", encoding="utf_8_sig",index=False)
    Tool.SaveDatabase(gr_df,"D")