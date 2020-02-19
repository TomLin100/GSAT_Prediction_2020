# -*- coding: utf-8 -*-
"""
Created on Sat Feb 15 00:37:29 2020

@author: jialing
"""
import pandas as pd

def grvsdurl():
    gr=open('OutputGSAT.csv','r',encoding='utf-8-sig')
    dd=open('OutputDURL.csv','r',encoding='utf-8-sig')
    gr_did = list()#存簡章的DID
    gr_school = list()#存簡章的學校名稱
    gr_first_school = list()

    dd_school = list()#學校名稱系名
    dd_link = list()#學校網址
    dd_first_school = list()
    
    # =============================================================================
    # 讀取簡章及學群學類的校名跟科系名
    # =============================================================================
    header = next(gr)
    for x in gr:
        x = x.strip("\n")
        x = x.split(",")
        gr_did.append(x[0])#簡章校系代碼
        gr_first_school.append(x[1]+x[3])#簡章學校名稱
        
    header = next(dd)
    for y in dd:
        y = y.strip("\n")
        y = y.split(",")
        dd_first_school.append(y[1])#學群學類學校名稱
        dd_link.append(y[2])#學群學類科系名稱
    
    did=[]
    school=[]
    link=[]
    is_data=[]
    no_did=[]
    no_school=[]
    #把學群學類的科系名去雜訊
    for cl in dd_first_school:
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
        dd_school.append(cl.strip())
    
    for gr in gr_first_school:
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
        gr_school.append(gr.strip())
    
    for a in range(len(gr_did)):
        for b in range(len(dd_school)):
            if gr_did[a] in is_data:
                pass
            elif gr_school[a] == dd_school[b]:
                is_data.append(gr_did[a])
                did.append(gr_did[a])
                school.append(gr_school[a])
                link.append(dd_link[b])
            else:
                gg=gr_school[a].split(" ")
                if gg[0]== dd_school[b]:
                    is_data.append(gr_did[a])
                    did.append(gr_did[a])
                    school.append(gr_school[a])
                    link.append(dd_link[b])
    
    #沒有對到的簡章校系代碼及資訊
        if gr_did[a] in is_data:
            pass
        else:
            no_did.append(gr_did[a])
            no_school.append(gr_school[a])
    
    data_df=pd.DataFrame({"DID":did,"DURL":link})
    data_df.to_csv('OutputGrVsDURL.csv',encoding='utf-8-sig',index=False)