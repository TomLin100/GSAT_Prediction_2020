# -*- coding: utf-8 -*-
"""
Created on Mon Feb 10 21:21:40 2020

@author: jialing
"""

import pandas as pd
import Tool

def citypp(url):
    soup = Tool.VisitWebsite(url)
    
    school_name=[]
    school_city=[]
    school_pp=[]
    
    find_dl=soup.findAll('dl')
    for dl in find_dl:
        all_data=dl.get_text()
    for data in all_data.split():
        if "縣" in data:
            if len(data)<5:
                city=data
        elif "市" in data:
            if len(data)<5:
                city=data
    
        if "私立" in data:
            if "(淡水工商)" in data:
                data=data.strip("(淡水工商)" )
                school_name.append(data.strip("私立"))
                school_city.append(city.strip())
                school_pp.append("私立")
            elif "(臺中健管)" in data:
                data=data.strip("(臺中健管)")
                school_name.append(data.strip("私立"))
                school_city.append(city.strip())
                school_pp.append("私立")
            else:
                school_name.append(data.strip("私立"))
                school_city.append(city.strip())
                school_pp.append("私立")
        elif "國立" in data:
            school_name.append(data.strip())
            school_city.append(city)
            school_pp.append("公立")
        else:
            if len(data)<4:
                pass
            else:
                school_name.append(data.strip())
                school_city.append(city)
                school_pp.append("私立")
    if "臺北基督學院" not in school_name:
        school_name.append("臺北基督學院")
        school_city.append("新北市")
        school_pp.append("私立")
    data_df=pd.DataFrame({"學校名稱":school_name,"縣市":school_city,\
                          "PP":school_pp})
    data_df.to_csv('OutputCityPp.csv',encoding='utf-8-sig')