# -*- coding: utf-8 -*-
"""
Created on Thu Jan 23 11:14:58 2020

@author: jialing
"""

import pandas as pd
import Tool

def collego(all_url):
    all_link=[]
    
    soup_all=Tool.VisitWebsite(all_url)
    find_a_box_item=soup_all.findAll('a',class_="box__item")
    
    collego_group=[]#學群 +學類
    collego_class=[]#學類 +學群
    
    collego_school_name=[]#學校
    collego_department_name=[]#系組名稱
    collego_school_class=[]#學類
    class__group=[]#放學群+學類 確認是否重複

    for a in find_a_box_item:
        find_link=a.get('href')
        all_link.append('https://collego.ceec.edu.tw/'+find_link)

    url="https://collego.ceec.edu.tw/Highschool/MajorIntro?current_major_id=1&collegeFrom=1"    

    #因為有不分系的
    all_link.append('https://collego.ceec.edu.tw/Highschool/CollegeIntro?current_college_id=19')
    for url in all_link:
        soup = Tool.VisitWebsite(url)
        find_b=soup.findAll('b',style="font-size:22pt")#找學類
        for b in find_b:
            bt=b.get_text().split()

        if len(bt)==1:
            page_class=str(bt[0])
        elif len(bt)==2:
            page_class=str(bt[0]+bt[1])
        # =============================================================================
        # 學群+學類
        # =============================================================================

        find_a_target=soup.findAll('a',target="_blank")
        for tar in find_a_target:
            t=tar.get_text()#黑色粗體學類
            if "學群" in t:
                class_add_group=t+page_class
                if class_add_group in class__group:#學群學類在學群+學類裡的話就跳過，避免重複
                    pass
                else:
                    class__group.append(class_add_group)
                    collego_group.append(t)
                    collego_class.append(page_class)
            if "不分系" in t:
                class_add_group="不分系學群"
                if class_add_group in class__group:#學群學類在學群+學類裡的話就跳過，避免重複
                    pass
                else:
                    class__group.append(class_add_group)
                    collego_group.append("不分系學群")
                    collego_class.append("不分系學類")
        # =============================================================================
        # 學校+系組名稱+學類
        # =============================================================================
        find_td=soup.findAll('td')
        td_text=[]
        school_td=[]
        major_td=[]
        c=0
        for td in find_td:
            td_text.append(td.get_text().strip())
            data=td.get_text().strip()
            c+=1
            if c%3==1:
                school_td.append(data)
                collego_school_name.append(data)
                
            if c%3==2:
                if "不分系" in page_class:
                    major_td.append(data)
                    collego_department_name.append(data)
                    collego_school_class.append("不分系學類")
                else:
                    major_td.append(data)
                    collego_department_name.append(data)
                    collego_school_class.append(page_class)
                
    group_class_data_df=pd.DataFrame({"Cname":collego_class,"Gname":collego_group})
    group_class_data_df.to_csv('CG.csv',encoding='utf-8-sig')
    Tool.SaveDatabase(group_class_data_df,'CG')
    school_class_data_df=pd.DataFrame({"school_name":collego_school_name,"major_name":collego_department_name,"major_class":collego_school_class})
    school_class_data_df.to_csv('OutputSC.csv',encoding='utf-8-sig')