# -*- coding: utf-8 -*-
"""
Created on Thu Jul 11 11:37:49 2019

@author: jialing
"""
import pandas as pd
import Tool

def grvsclass():
    gr=open('OutputGSAT.csv','r',encoding='utf-8-sig')
    cl=open('OutputSC.csv','r',encoding='utf-8-sig')
    gr_did = list()#存簡章的DID
    gr_school = list()#存簡章的學校名稱
    gr_first_major = list()#存簡章的學校名稱
    
    cl_school = list()#存學群學類的學校名稱
    cl_first_major = list()#存學群學類的科系名稱
    cl_class = list()#學群學類的學類
    # =============================================================================
    # 讀取簡章及學群學類的校名跟科系名
    # =============================================================================
    header = next(gr)
    for x in gr:
        x = x.strip("\n")
        x = x.split(",")
        gr_did.append(x[0])#簡章校系代碼
        gr_school.append(x[1])#簡章學校名稱
        gr_first_major.append(x[3])#簡章科系名稱

    header = next(cl)
    for y in cl:
        y = y.strip("\n")
        y = y.split(",")
        cl_school.append(y[1])#學群學類學校名稱
        cl_first_major.append(y[2])#學群學類科系名稱
        cl_class.append(y[3])

    final_class=[]
    final_did=[]
    final_major=[]
    final_school=[]
    gr_fi_school=[]
    gr_fi_major=[]
    no_final_class=[]
    no_final_major=[]
    no_final_school=[]
    no_gr_fi_major=[]
    no_gr_fi_school=[]
    no_final_did=[]
    cl_major=[]
    gr_major=[]
    #把學群學類的科系名去雜訊
    for cl in cl_first_major:
        cl=cl.replace("(尚未參與問卷調查)","")
        cl=cl.replace("(問卷填答中)","")
        cl=cl.replace("(","")
        cl=cl.replace(")","")
        cl=cl.replace("學系","學系 ")
        cl=cl.replace("學學系","學系 ")
        cl=cl.replace("組","組 ")
        cl=cl.replace("臺北校區","")
        cl=cl.replace("台北校區","")
        cl=cl.replace("桃園校區","")
        cl=cl.replace("臺北","")
        cl=cl.replace("台北","")
        cl=cl.replace("桃園","")
        cl=cl.replace("青年儲蓄帳戶組","")
        cl=cl.replace("-類繁星組","")
        cl=cl.replace("-一般組","")
        cl=cl.replace("．","")
        cl_major.append(cl.strip())
    
    for gr in gr_first_major:
        gr=gr.replace("(","")
        gr=gr.replace(")","")
        gr=gr.replace("學系","學系 ")
        gr=gr.replace("學學系","學系 ")
        gr=gr.replace("組","組 ")
        gr=gr.replace("臺北校區","")
        gr=gr.replace("台北校區","")
        gr=gr.replace("桃園校區","")
        gr=gr.replace("臺北","")
        gr=gr.replace("台北","")
        gr=gr.replace("桃園","")
        gr=gr.replace("青年儲蓄帳戶組","")
        gr=gr.replace("-類繁星組","")
        gr=gr.replace("-一般組","")
        gr=gr.replace("．","")
        gr_major.append(gr.strip())
    is_data=[]#用來放已經有的DID
    
    for a in range(len(gr_did)):
        for b in range(len(cl_major)):
            if gr_did[a] in is_data:
                pass
            elif gr_school[a] == cl_school[b]:#學校相同
                if gr_major[a] == cl_major[b]:#科系相同
                    is_data.append(gr_did[a])
                    final_class.append(cl_class[b])
                    final_major.append(cl_major[b])
                    final_school.append(cl_school[b])
                    gr_fi_major.append(gr_major[a])
                    gr_fi_school.append(gr_school[a])
                    final_did.append(gr_did[a])
                elif gr_major[a][0] == cl_major[b][0] :#拿科系相比
                    is_data.append(gr_did[a])
                    final_class.append(cl_class[b])
                    final_major.append(cl_major[b])
                    final_school.append(cl_school[b])
                    gr_fi_major.append(gr_major[a])
                    gr_fi_school.append(gr_school[a])
                    final_did.append(gr_did[a])
                    
    #沒有對到的簡章校系代碼及資訊
        if gr_did[a] in is_data:
            pass
        else:
            no_final_class.append(cl_class[b])
            no_final_major.append(cl_major[b])
            no_final_school.append(cl_school[b])
            no_gr_fi_major.append(gr_major[a])
            no_gr_fi_school.append(gr_school[a])
            no_final_did.append(gr_did[a])

    data_df=pd.DataFrame({"DID":final_did,"Cname":final_class})
    Tool.SaveDatabase(data_df,'DC')
    data_df.to_csv('DC.csv',encoding='utf-8-sig',index=False)