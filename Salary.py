# -*- coding: utf-8 -*-
"""
Created on Wed Sep  4 17:12:20 2019

@author: jialing
"""

import pandas as pd
import time
import Tool

def salary(url):
    soup = Tool.VisitWebsite(url)
    i=0
    school_list=[]
    school_list2=[]
    
    for link in soup.find_all('a'):
        link_a = link.get('href')
        school_link='https://www.104.com.tw'+str(link_a) 
        school_name=link.get_text()
        if(i>0):
            school_list.append(school_name)
            school_list2.append(school_link)
        i+=1
    school_data_df=pd.DataFrame({"school_name":school_list,"school_link":school_list2})
    
    pd.set_option('display.width', 100000)  # 设置字符显示宽度
    pd.set_option('display.max_rows', None)  # 设置显示最大列
    major_data_df_all=pd.DataFrame()
    l=0
    for n in school_data_df.school_link:
        soup=Tool.VisitWebsite(n)
        j=0
        major_name_list=[]
        major_link_list=[]
        school_list_name=[]
        for li in soup.find_all('a'):
            link_b = li.get('href')
            major_link='https://www.104.com.tw'+str(link_b)
            major_name=li.get_text()
            if(j>2):
                school_list_name.append(school_data_df.school_name[l])
                major_name_list.append(major_name)
                major_link_list.append(major_link)
            j+=1
        major_data_df=pd.DataFrame({"school_name":school_list_name,"major_name":major_name_list,"major_link":major_link_list})
        l+=1
        major_data_df_all=major_data_df_all.append(major_data_df,ignore_index=True)
    
    pd.set_option('display.max_column', None)  # 设置显示最大行
    salary_list=[]
    salary_data_df_all=pd.DataFrame()
    for s in major_data_df_all.major_link:
        
        time.sleep(4)
        soup = Tool.VisitWebsite(s)
        sle_number=soup.find_all("div",class_="arrow-box-right cf hide")#取出要的值(左邊)
        data_list=[]
        for x in sle_number:
            percent_data=x.findAll("strong")
            for y in percent_data:
                data_number=y.get_text()
                data_list.append(data_number)
    
        if(data_list==[]):
            data_list.append(-1)
            salary=0
        else:
            sum_ = float(data_list[0]) * float(data_list[1])
            for i in range(0,6):
                sum_+=(float(data_list[(i+1)*2])-float(data_list[2*i]))* float(data_list[2*i+3])
            salary=int(sum_/100)
        salary_list.append(salary)

        time.sleep(30)

    salary_data_df_all=pd.DataFrame({"school_name":major_data_df_all.school_name,"major_name":major_data_df_all.major_name,"major_link":major_data_df_all.major_link,"salary":salary_list})
    salary_data_df_all.to_csv('OutputSalary.csv',encoding='utf-8-sig')