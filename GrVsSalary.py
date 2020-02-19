# -*- coding: utf-8 -*-
"""
Created on Thu Jul 11 11:37:49 2019

@author: jialing
"""
import pandas as pd

def grvssalary():
    gr=open('OutputGSAT.csv','r',encoding='utf-8-sig')
    sa=open('OutputSalary.csv','r',encoding='utf-8-sig')
    print(gr)
    gr_did = list()#存簡章的DID
    gr_school = list()#存簡章的學校名稱
    gr_first_major = list()#存簡章的學校名稱
    
    sa_first_school = list()#104的學校名稱
    sa_first_major = list()#104的科系名稱
    
    sa_salary = list()#104平均薪資
    sa_link = list()#104薪資的網址
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
    print(gr_first_major)
    header = next(sa)
    for y in sa:
        y = y.strip("\n")
        y = y.split(",")
        sa_first_school.append(y[1])#學群學類學校名稱
        sa_first_major.append(y[2])#學群學類科系名稱
        sa_link.append(y[3])
        sa_salary.append(y[4])
        
    final_link=[]
    final_salary=[]
    final_did=[]
    final_major=[]
    final_school=[]
    gr_fi_school=[]
    gr_fi_major=[]
    no_final_link=[]
    no_final_major=[]
    no_final_school=[]
    no_gr_fi_major=[]
    no_gr_fi_school=[]
    no_final_did=[]
    gr_major=[]
    sa_major=[]
    sa_school=[]
    step=[]#看哪階段比對到了
    
    #把學群學類的科系名去雜訊
    
    for gr in gr_first_major:
        gr=gr.replace("學系","學系 ")
        gr=gr.split(" ")[0]
        gr=gr.replace("臺灣語文學系","台灣語文學系")
        gr=gr.replace("臺灣文學系","台灣文學系")
        gr=gr.replace("醫學檢驗暨生物技術學系","醫學檢驗生物技術學系")
        gr=gr.replace("會計學系","會計與資訊科技學系")
        gr=gr.replace("材料科學與工程學系","材料科學學系")
        gr=gr.replace("醫學工程學系","生物醫學工程學系")
        gr=gr.replace("教育心理與輔導學系","輔導學系")
        gr=gr.replace("工業工程與管理學系","工業工程與科技系統工程學系")
        gr=gr.replace("公共行政暨政策學系","公共行政與政策學系")
        gr=gr.replace("動物科學系","動物科學學系")#
        gr=gr.replace("統計學系","統計科學學系")
        gr=gr.replace("聽力暨語言治療學系","聽力學與語言治療研究所")
        gr=gr.replace("醫藥暨應用化學系","醫藥化學系")
        gr=gr.replace("餐旅管理學系","餐旅行銷管理學系")
        gr=gr.replace("機械與機電工程學系","機電工程學系")
        gr=gr.replace("電子工程學系","電子學系")
        gr=gr.replace("資訊傳播學系","資訊傳播工程學系")
        gr=gr.replace("會計與資訊學系","會計與資訊學系")
        gr=gr.replace("華語文學系","華語學系")
        gr=gr.replace("通訊工程學系","通訊學系")
        gr=gr.replace("國際貿易學系","國際貿易暨商務學系")
        gr=gr.replace("風險管理與保險學系","風險管理學系")
        gr=gr.replace("英美語文學系","英美文學系")
        gr=gr.replace("光電科學與工程學系","光電工程學系")
        gr=gr.replace("休閒運動管理學系","休閒運動與管理學系")
        gr=gr.replace("生物生物醫學工程學系","生物醫學工程學系")
        gr=gr.replace("化學工程與材料工程學系","化學系")
        gr=gr.replace("地質科學系","地質學系")
        gr=gr.replace("犯罪防治學系","犯罪學系")
        gr=gr.replace("國際企業管理學系","企業管理學系")
        gr=gr.replace("會計資訊學系","會計與資訊科技學系")
        gr=gr.replace("電腦與通訊學系","電腦通訊學系")
    
        gr_major.append(gr.strip())
        
    is_data=[]#用來放已經有的DID
    
    for sa in sa_first_school:
        sa = sa.replace("私立","")
        sa = sa.replace("(淡水工商)","")#真理大學
        sa = sa.replace("(臺中健管)","")#亞洲大學
        sa_school.append(sa.strip())
    for saa in sa_first_major:
        saa=saa.replace("臺灣語文學系","台灣語文學系")
        saa=saa.replace("臺灣文學系","台灣文學系")
        saa=saa.replace("生物資訊與醫學工程學系","生物醫學工程學系")#私立亞洲大學(臺中健管)	生物資訊與醫學工程學系
        sa_major.append(saa.strip())
    for a in range(len(gr_did)):
        for b in range(len(sa_school)):
            if gr_did[a] in is_data:
                pass
            elif gr_school[a] == sa_school[b]:#學校相同
                if gr_major[a]== sa_major[b]:#科系相同
                    gr_fi_major.append(gr_major[a])
                    gr_fi_school.append(gr_school[a])
                    final_did.append(gr_did[a])
                    final_school.append(sa_school[b])
                    final_major.append(sa_major[b])
                    final_link.append(sa_link[b])
                    final_salary.append(sa_salary[b])
                    is_data.append(gr_did[a])
                    step.append("學校一樣，科系一樣")
                elif gr_major[a]=="歷史學系":#拿科系相比
                    if sa_major[b]=="史學系":
                        gr_fi_major.append(gr_major[a])
                        gr_fi_school.append(gr_school[a])
                        final_did.append(gr_did[a])
                        final_school.append(sa_school[b])
                        final_major.append(sa_major[b])
                        final_link.append(sa_link[b])
                        final_salary.append(sa_salary[b])
                        is_data.append(gr_did[a])
                        step.append("歷史學系")
                elif gr_major[a]=="中國語文學系" or gr_major[a]=="中國文學系" or gr_major[a]=="中國文學學系":#拿科系相比
                    if sa_major[b]== "國文學系":
                        gr_fi_major.append(gr_major[a])
                        gr_fi_school.append(gr_school[a])
                        final_did.append(gr_did[a])
                        final_school.append(sa_school[b])
                        final_major.append(sa_major[b])
                        final_link.append(sa_link[b])
                        final_salary.append(sa_salary[b])
                        is_data.append(gr_did[a])
                        step.append("國文學系")
                elif gr_major[a].replace("學系","系")== sa_major[b]:
                    gr_fi_major.append(gr_major[a])
                    gr_fi_school.append(gr_school[a])
                    final_did.append(gr_did[a])
                    final_school.append(sa_school[b])
                    final_major.append(sa_major[b])
                    final_link.append(sa_link[b])
                    final_salary.append(sa_salary[b])
                    is_data.append(gr_did[a])
                    step.append("學系,系")
                elif gr_major[a].replace("學系","學學系")== sa_major[b]:
                    gr_fi_major.append(gr_major[a])
                    gr_fi_school.append(gr_school[a])
                    final_did.append(gr_did[a])
                    final_school.append(sa_school[b])
                    final_major.append(sa_major[b])
                    final_link.append(sa_link[b])
                    final_salary.append(sa_salary[b])
                    is_data.append(gr_did[a])
                    step.append("學系,學學系")
                elif gr_major[a].replace("學系","學位學程")== sa_major[b]:
                    gr_fi_major.append(gr_major[a])
                    gr_fi_school.append(gr_school[a])
                    final_did.append(gr_did[a])
                    final_school.append(sa_school[b])
                    final_major.append(sa_major[b])
                    final_link.append(sa_link[b])
                    final_salary.append(sa_salary[b])
                    is_data.append(gr_did[a])
                    step.append("學系,學位學程")
                elif gr_major[a][:4]==sa_major[b][:4]:
                    gr_fi_major.append(gr_major[a])
                    gr_fi_school.append(gr_school[a])
                    final_did.append(gr_did[a])
                    final_school.append(sa_school[b])
                    final_major.append(sa_major[b])
                    final_link.append(sa_link[b])
                    final_salary.append(sa_salary[b])
                    is_data.append(gr_did[a])
                    step.append("[:4]")

    #沒有對到的簡章校系代碼及資訊
        if gr_did[a] in is_data:
            pass
        else:
            no_final_did.append(gr_did[a])
            no_final_school.append(sa_school[b])
            no_final_major.append(sa_major[b][0])
            no_final_link.append(sa_school[b])
            no_gr_fi_major.append(gr_major[a])
            no_gr_fi_school.append(gr_school[a])

    data_df=pd.DataFrame({"DID":final_did,"SalaryURL":final_link,\
                          "Salary":final_salary,"step":step})
    data_df.to_csv('OutputGrVsSalary.csv',encoding='utf-8-sig',index=False)
