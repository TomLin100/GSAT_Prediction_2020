# -*- coding: utf-8 -*-
"""
Created on Sat Feb 15 00:11:35 2020

@author: jialing
"""
import pandas as pd

def grvsuurl():
    gr=open('OutputGSAT.csv','r',encoding='utf-8-sig')
    ud=open('OutputUURL.csv','r',encoding='utf-8-sig')
    gr_did = list()#存簡章的DID
    gr_school = list()#存簡章的學校名稱
    
    ud_school = list()#學校名稱
    ud_link = list()#學校網址
    
    header = next(gr)
    for x in gr:
        x = x.strip("\n")
        x = x.split(",")
        gr_did.append(x[0])#簡章校系代碼
        gr_school.append(x[1])#簡章學校名稱
    
    header = next(ud)
    for y in ud:
        y = y.strip("\n")
        y = y.split(",")
        ud_school.append(y[1])#學群學類學校名稱
        ud_link.append(y[2])#學群學類科系名稱
#    print(ud_link)
    did=[]
    school=[]
    link=[]
    is_data=[]
    no_did=[]
    no_school=[]
    for a in range(len(gr_did)):
        for b in range(len(ud_school)):
            if gr_school[a]==ud_school[b]:
                is_data.append(gr_did[a])
                did.append(gr_did[a])
                school.append(gr_school[a])
                link.append(ud_link[b])
        if gr_did[a] in is_data:
            pass
        else:
            no_did.append(gr_did[a])
            no_school.append(gr_school[a])

    data_df=pd.DataFrame({"DID":did,"UURL":link})
    data_df.to_csv('OutputGrVsUURL.csv',encoding='utf-8-sig',index=False)