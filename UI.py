# -*- coding: utf-8 -*-
"""
Created on Sat Feb 15 19:44:22 2020

@author: jialing
"""
import time
import tkinter as tk
import GSAT
import CityPp
import Salary
import Collego
import UURL
import DURL

import GrVsUURL
import GrVsDURL
import GrVsClass
import GrVsSalary
import GrVsCityPP

import Merge
import Downloadfile
import convertT
import NewScoreData
import OldScoreData
import DeleteTable

window = tk.Tk()
window.title('學測落點分析資料整理')
window.geometry('300x100')

url_university='https://university-tw.ldkrsi.men/caac/#gsc.tab=0'
url_104='https://www.104.com.tw/jb/career/department/navigation?browser=1&degree=3'
url_collego_m='https://collego.ceec.edu.tw/Highschool/MajorList'
url_collego_s='https://collego.ceec.edu.tw/Highschool/School'

def BaseDatabase():
    GSAT.gsat(url_university)
    time.sleep(30)
    CityPp.citypp(url_104)
    time.sleep(30)
    Salary.salary(url_104)
    time.sleep(30)
    Collego.collego(url_collego_m)
    time.sleep(30)
    UURL.uurl(url_collego_s)
    time.sleep(30)
    DURL.durl()
    time.sleep(30)
    GrVsUURL.grvsuurl()
    GrVsDURL.grvsdurl()
    GrVsClass.grvsclass()
    GrVsSalary.grvssalary()
    GrVsCityPP.grvscitypp()
    Merge.merge()
    tk.messagebox.showinfo(title='注意', message='D資料表完成！')
    
def UpdateSalary():
    Salary.salary(url_104)
    Merge.merge()
    DeleteTable.deletetable()
    tk.messagebox.showinfo(title='注意', message='完成更新薪資資料！')

def UpdateDatabase():
    Downloadfile.downloadfile()
    convertT.convertt()
    NewScoreData.newscoredata()
    OldScoreData.oldscoredata()
    tk.messagebox.showinfo(title='注意', message='完成更新資料庫！')
    
btn = tk.Button(window, text='產生測試資料庫',command=BaseDatabase)
btn.pack()
btn = tk.Button(window, text='更新薪資資料',command=UpdateSalary)
btn.pack()
btn = tk.Button(window, text='產生正式資料庫',command=UpdateDatabase)
btn.pack()
window.mainloop()