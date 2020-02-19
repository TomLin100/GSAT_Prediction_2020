# -*- coding: utf-8 -*-
"""
Created on Mon Feb 10 21:48:30 2020

@author: jialing
"""

import pandas as pd

def grvscitypp():
    gr=open('OutputGSAT.csv','r',encoding='utf-8-sig')
    ci=open('OutputCityPp.csv','r',encoding='utf-8-sig')
    
    gr_did = list()#存簡章的DID
    gr_school = list()#存簡章的學校名稱
    
    ci_school = list()#學校名稱
    ci_city = list()#104的縣市
    ci_pp = list()#104的公私立
    
    # =============================================================================
    # 讀取簡章及學群學類的校名跟科系名
    # =============================================================================
    header = next(gr)
    for x in gr:
        x = x.strip("\n")
        x = x.split(",")
        gr_did.append(x[0])#簡章校系代碼
        gr_school.append(x[1])#簡章學校名稱
    
    header = next(ci)
    for y in ci:
        y = y.strip("\n")
        y = y.split(",")
        ci_school.append(y[1])#學群學類學校名稱
        ci_city.append(y[2])#104的縣市
        ci_pp.append(y[3])#104的公私立
    did=[]
    school=[]
    city=[]
    pp=[]
    is_data=[]#用來放已經有的DID
    no_did=[]
    no_school=[]
    for a in range(len(gr_did)):
        for b in range(len(ci_school)):
            if gr_school[a] == ci_school[b]:#學校相同
                is_data.append(gr_did[a])
                did.append(gr_did[a])
                school.append(gr_school[a])
                city.append(ci_city[b])
                pp.append(ci_pp[b])
        if gr_did[a] in is_data:
            pass
        else:
            no_did.append(gr_did[a])
            no_school.append(gr_school[a])

    data_df=pd.DataFrame({"DID":did,"City":city,"PP":pp})
    data_df.to_csv('OutputGrVsCityPP.csv',encoding='utf-8-sig',index=False)