# -*- coding: utf-8 -*-
"""
Created on Sat Feb 15 11:57:05 2020

@author: jialing
"""
import urllib.request;
import urllib.error;
from bs4 import BeautifulSoup;
import socket;

def downloadfile():
    socket.setdefaulttimeout(30); #設定socket超過時間
    header = {"user-Agent" : "Mozilla/5.0"};
    url = "http://www.ceec.edu.tw/files/file_pool/1/0J191625436682984511/22%E5%90%84%E7%A7%91%E7%B4%9A%E5%88%86%E4%BA%BA%E6%95%B8%E5%88%86%E5%B8%83%E8%A1%A8108.xls";
    url2 = "http://www.ceec.edu.tw/files/file_pool/1/0J191625424870257539/26%E5%90%84%E7%A7%91%E6%88%90%E7%B8%BE%E6%A8%99%E6%BA%96%E4%B8%80%E8%A6%BD%E8%A1%A8108.xls";
    
    request = urllib.request.Request(url, headers=header);
    response = urllib.request.urlopen(request);
    soup = BeautifulSoup(response, "html.parser");
    
    from urllib.request import urlretrieve;
    urlretrieve(url, ".22各科級分人數分布表.xls");
    urlretrieve(url2, ".26各科成績標準一覽表.xls");
    response.close();