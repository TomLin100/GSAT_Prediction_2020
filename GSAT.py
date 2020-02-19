import requests;
import pandas as pd;
import re;
from bs4 import BeautifulSoup;

def getField(storeList, seq, td):    #storeList為儲存的list，seq為要取得資料的td, 要擷取的資料集
    count = 0;    #計算目前欄位   
    for data in td :
        count = count + 1;
        if count % 34  == seq :
            storeList.append(data.text.strip());
    return storeList;

#將頂標、前標...轉為數字
def translateStandard(targetList):
    for i in range(len(targetList)):
        if("頂" in targetList[i]):
            targetList[i] = "5";
        elif("前" in targetList[i]):
            targetList[i] = "4";
        elif("均" in targetList[i]):
            targetList[i] = "3";
        elif("後" in targetList[i]):
            targetList[i] = "2";
        elif("底" in targetList[i]):
            targetList[i] = "1";
        elif(targetList[i].isdigit()):
            pass;
        else:
            targetList[i] = "0";
    return targetList;
def gsat(url):
#    url = "https://university-tw.ldkrsi.men/caac/#gsc.tab=0";
    response = requests.get(url, verify=False);
    
    bs = BeautifulSoup(response.text, "html.parser");    #將網頁內容用html.parser解析成beautifulSoup物件
    content = bs.prettify();    #將bs進行格式化為字串;
    
    schoolNames = [];
    schoolUrl = [];
    
    for link in bs.find_all("a"):
        if(str.isdigit(link.get("href"))):
            schoolNames.append(link.get_text());
            schoolUrl.append("https://university-tw.ldkrsi.men/caac/"+str(link.get("href"))+"#gsc.tab=0");
    
    #依欄位名稱將資料放入對應list 
    did_link = [];    #代碼連結
    _id = [];    #代碼
    uName = [];    #學校名稱
    dName = [];    #科系名稱
    quota = [];    #招收人數
    chinese = [];    #國文檢定標準
    english = [];    #英文檢定標準
    math = [];    #數學檢定標準
    social = [];    #社會檢定標準
    science = [];    #自然檢定標準
    listen = [];    #英文聽力檢定標準
    mag_ch = [];    #篩選倍率_國文
    mag_en = [];    #篩選倍率_英文
    mag_ma = [];    #篩選倍率_數學
    mag_so = [];    #篩選倍率_社會
    mag_sc = [];    #篩選倍率_自然
    addition = [];    #相加項
    last_quota = [];    #去年招收人數
    last_chinese = [];    #去年國文檢定標準
    last_english = [];    #去年英文檢定標準
    last_math = [];    #去年數學檢定標準
    last_social = [];    #去年社會檢定標準
    last_science = [];    #去年自然檢定標準
    last_listen = [];    #去年英文聽力檢定標準
    last_all = [];    #去年總分檢定標準
    last_mag_ch = [];    #去年篩選倍率_國文
    last_mag_en = [];    #去年篩選倍率_英文
    last_mag_ma = [];    #去年篩選倍率_數學
    last_mag_so = [];    #去年篩選倍率_社會
    last_mag_sc = [];    #去年篩選倍率_自然
    last_mag_all = [];    #去年篩選倍率_總分
    last_addition = [];   #去年篩選倍率_相加項
    filter_1 = [];    #篩選一
    filter_2 = [];    #篩選二
    filter_3 = [];    #篩選三
    filter_4 = [];    #篩選四
    filter_5 = [];    #篩選五
    overfilter = [];    #超額篩選
    
    #逐筆取出網頁內容 
    for url in schoolUrl:
        response = requests.get(url, verify=False);
        bs = BeautifulSoup(response.text,"html.parser");
        td = bs.select("td");
        title = bs.find("h1");  #抓網頁的 h1(校名)
        school_title = title.text;  #抓出校名的文字
        school_title.find("年");
        school_title = school_title.replace(school_title[0:school_title.find("年")+1],'').strip();
        school_title = school_title.strip("個人申請");
        
        #把該學校的校系分則連結取出並存入did_link 
        for href in bs.findAll("a"): 
            
            #如果包含"https://www.cac.edu.tw/apply"和"/system/"
            url = "https://www.cac.edu.tw/apply";
            if url in href.get("href"):
                if 'html' in href.get("href"):
                    did_link.append(href.get("href"));
    
        _id = getField(_id, 1, td);    #取出校系代碼並存入_id    
        dName = getField(dName, 2, td);#科系
        quota = getField(quota, 3, td);#招收人數
        chinese = getField(chinese , 4, td);#檢定標準-國
        english = getField(english, 5, td);#檢定標準-英
        math = getField(math, 6, td);#檢定標準-數
        social = getField(social, 7, td);#檢定標準-社
        science = getField(science, 8, td);#檢定標準-自
        listen = getField(listen, 9, td);#檢定標準-英聽
        mag_ch = getField(mag_ch, 10, td);#篩選倍率-國
        mag_en = getField(mag_en, 11, td);#篩選倍率-英
        mag_ma = getField(mag_ma, 12, td);#篩選倍率-數
        mag_so = getField(mag_so, 13, td);#篩選倍率-社
        mag_sc = getField(mag_sc, 14, td);#篩選倍率-自
        addition = getField(addition, 15, td);#篩選倍率-相加項
        last_quota = getField(last_quota, 16, td);#去年招收人數
        last_chinese = translateStandard(getField(last_chinese, 17, td));#去年檢定標準-國
        last_english = translateStandard(getField(last_english, 18, td));#去年檢定標準-英
        last_math = translateStandard(getField(last_math, 19, td));#去年檢定標準-數
        last_social = translateStandard(getField(last_social, 20, td));#去年檢定標準-社
        last_science = translateStandard(getField(last_science, 21, td));#去年檢定標準-自
        last_listen = getField(last_listen, 22, td);#去年檢定標準-英聽
    #    last_all = getField(last_all, 23, td);
        last_mag_ch = getField(last_mag_ch, 23, td);#去年篩選倍率-國
        last_mag_en = getField(last_mag_en, 24, td);#去年篩選倍率-英
        last_mag_ma = getField(last_mag_ma, 25, td);#去年篩選倍率-數
        last_mag_so = getField(last_mag_so, 26, td);#去年篩選倍率-社
        last_mag_sc = getField(last_mag_sc, 27, td);#去年篩選倍率-自
        last_addition = getField(last_addition, 28, td);#去年篩選倍率-相加項
        filter_1 = getField(filter_1, 29, td);#去年篩選1
        filter_2 = getField(filter_2, 30, td);#去年篩選2
        filter_3 = getField(filter_3, 31, td);#去年篩選3
        filter_4 = getField(filter_4, 32, td);#去年篩選4
        filter_5 = getField(filter_5, 33, td);#去年篩選5
        overfilter = getField(overfilter, 0, td);#超額篩選
        for i in range(len(_id) - len(uName)):    #將學校名稱填入list
            uName.append(school_title);
    
    
    #將list對應欄位名稱存入字典 
    data_dict = {"科系代碼連結" : did_link,
                 "科系代碼" : _id,
                 "學校名稱" : uName,
                 "科系名稱" : dName,
                 "招收人數" : quota,
                 "國文檢定標準" : chinese,
                 "英文檢定標準" : english,
                 "數學檢定標準" : math,
                 "社會檢定標準" : social,
                 "自然檢定標準" : science,
                 "英文聽力檢定標準" : listen,
                 "篩選倍率_國文" : mag_ch,
                 "篩選倍率_英文" : mag_en,
                 "篩選倍率_數學" : mag_ma,
                 "篩選倍率_社會" : mag_so,
                 "篩選倍率_自然" : mag_sc,
                 "篩選倍率_相加項" : addition,
                 "去年招收人數" : last_quota,
                 "去年國文檢定標準" : last_chinese,
                 "去年英文檢定標準" : last_english,
                 "去年數學檢定標準" : last_math,
                 "去年社會檢定標準" : last_social,
                 "去年自然檢定標準" : last_science,
                 "去年英文聽力檢定標準" : last_listen,
    #             "去年總分檢定標準" : last_all,
                 "去年篩選倍率_國文" : last_mag_ch,
                 "去年篩選倍率_英文" : last_mag_en,
                 "去年篩選倍率_數學" : last_mag_ma,
                 "去年篩選倍率_社會" : last_mag_so,
                 "去年篩選倍率_自然" : last_mag_sc,
    #             "去年篩選倍率_總分" : last_mag_all,
                 "去年篩選倍率_相加項":last_addition,
                 "篩選一" : filter_1,
                 "篩選二" : filter_2,
                 "篩選三" : filter_3,
                 "篩選四" : filter_4,
                 "篩選五" : filter_5,
                 "超額篩選" : overfilter};
    
    #擷取完畢--------
    #處理擷取後資料
    DID = _id;
    UName = uName;    #學校名稱
    DName = dName;    #科系名稱
    #TL1 = chinese;    #學測等第-國文
    #TL2 = english;    #學測等第-英文
    #TL3 = math;    #學測等第-數學
    #TL4 = social;    #學測等第-社會
    #TL5 = science;    #學測等第-自然
    #TL6 = ["0"] * len(DID);    #學測等第-總級分
    ELLEVEL = listen;    #英聽門檻
    Change = [0] * len(DID);    #與去年學測不同的地方
    lastCriterion = [0] * len(DID);    #去年最低錄取級分
    rateOfThisYear = [0] * len(DID);    #今年的採計倍率
    ExamURL = did_link;    #學測校系分則網址
    
    #將檢定標準轉為數字，例：頂標 -> 5，英聽亦同
    chinese = translateStandard(chinese);
    english = translateStandard(english);
    math = translateStandard(math);
    social = translateStandard(social);
    science = translateStandard(science);
    for i in range(len(ELLEVEL)):
        ELLEVEL[i] = ELLEVEL[i].upper();
        if(("A" in ELLEVEL[i]) or ("B" in ELLEVEL[i]) or ("C" in ELLEVEL[i]) or ("F" in ELLEVEL[i])):
            continue;
        else:
            ELLEVEL[i] = "N";
    
    #整理今年與去年的差異，Change欄位
    for i in range(len(DID)):
        Change[i] = "";
        
        if(not(quota[i] in last_quota[i])):
            Change[i] = Change[i] + "錄取人數改變, ";
        if(not(chinese[i] in last_chinese[i])):
            Change[i] = Change[i] + "檢定標準改變, ";
        elif(not(english[i] in last_english[i])):
            Change[i] = Change[i] + "檢定標準改變, ";
        elif(not(math[i] in last_math[i])):
            Change[i] = Change[i] + "檢定標準改變, ";
        elif(not(social[i] in last_social[i])):
            Change[i] = Change[i] + "檢定標準改變, ";
        elif(not(science[i] in last_science[i])):
            Change[i] = Change[i] + "檢定標準改變, ";
        if(not(mag_ch[i] in last_mag_ch[i])):
            Change[i] = Change[i] + "篩選倍率改變, ";
        elif(not(mag_en[i] in last_mag_en[i])):
            Change[i] = Change[i] + "篩選倍率改變, ";
        elif(not(mag_ma[i] in last_mag_ma[i])):
            Change[i] = Change[i] + "篩選倍率改變, ";
        elif(not(mag_so[i] in last_mag_so[i])):
            Change[i] = Change[i] + "篩選倍率改變, ";
        elif(not(mag_sc[i] in last_mag_sc[i])):
            Change[i] = Change[i] + "篩選倍率改變, ";
        Change[i] = Change[i].strip(", ");
        
        
    #整理去年最低錄取級分，lastCriterion欄位
    for i in range(len(DID)):
        lastCriterion[i] = "";
        if(len(filter_1[i]) > 0 and not("-" in filter_1[i])):
            lastCriterion[i] = lastCriterion[i] + filter_1[i] + ", ";
        if(len(filter_2[i]) > 0 and not("-" in filter_2[i])):
            lastCriterion[i] = lastCriterion[i] + filter_2[i] + ", ";
        if(len(filter_3[i]) > 0 and not("-" in filter_3[i])):
            lastCriterion[i] = lastCriterion[i] + filter_3[i] + ", ";
        if(len(filter_4[i]) > 0 and not("-" in filter_4[i])):
            lastCriterion[i] = lastCriterion[i] + filter_4[i] + ", ";
        if(len(filter_5[i]) > 0 and not("-" in filter_5[i])):
            lastCriterion[i] = lastCriterion[i] + filter_5[i] + ", ";
        lastCriterion[i] = lastCriterion[i].strip(", ");
    
    #整理今年篩選倍率，rateOfThisYear欄位 
    for i in range(len(DID)):
        rateOfThisYear[i] = "";
        if(not("-" in mag_ch[i])):
            rateOfThisYear[i] = rateOfThisYear[i] + "國 * " + mag_ch[i] + ", ";
        if(not("-" in mag_en[i])):
            rateOfThisYear[i] = rateOfThisYear[i] + "英 * " + mag_en[i] + ", ";
        if(not("-" in mag_ma[i])):
            rateOfThisYear[i] = rateOfThisYear[i] + "數 * " + mag_ma[i] + ", ";
        if(not("-" in mag_so[i])):
            rateOfThisYear[i] = rateOfThisYear[i] + "社 * " + mag_so[i] + ", ";
        if(not("-" in mag_sc[i])):
            rateOfThisYear[i] = rateOfThisYear[i] + "自 * " + mag_sc[i] + ", ";
        if(not("-" in addition[i])):
            rateOfThisYear[i] = rateOfThisYear[i] + "(";
            if("國" in addition[i]):
                rateOfThisYear[i] = rateOfThisYear[i] + "國+";
            if("英" in addition[i]):
                rateOfThisYear[i] = rateOfThisYear[i] + "英+";
            if("數" in addition[i]):
                rateOfThisYear[i] = rateOfThisYear[i] + "數+";
            if("社" in addition[i]):
                rateOfThisYear[i] = rateOfThisYear[i] + "社+";
            if("自" in addition[i]):
                rateOfThisYear[i] = rateOfThisYear[i] + "自+";
            rateOfThisYear[i] = rateOfThisYear[i].strip("+");
            rateOfThisYear[i] = rateOfThisYear[i] + ") * ";
            rateOfThisYear[i] = rateOfThisYear[i] + re.findall("[0-9]", addition[i])[0];
    
    for i in range(len(DID)):    #整理字串，去除最後面的逗號
        rateOfThisYear[i] = rateOfThisYear[i].strip(", ");
        
    #31種組合
    C = [0] * len(DID);
    E = [0] * len(DID);
    M = [0] * len(DID);
    S = [0] * len(DID);
    N = [0] * len(DID);
    CE = [0] * len(DID);
    CM = [0] * len(DID);
    CS = [0] * len(DID);
    CN = [0] * len(DID);
    EM = [0] * len(DID);
    ES = [0] * len(DID);
    EN = [0] * len(DID);
    MS = [0] * len(DID);
    MN = [0] * len(DID);
    SN = [0] * len(DID);
    CEM = [0] * len(DID);
    CES = [0] * len(DID);
    CEN = [0] * len(DID);
    CMS = [0] * len(DID);
    CMN = [0] * len(DID);
    CSN = [0] * len(DID);
    EMS = [0] * len(DID);
    EMN = [0] * len(DID);
    ESN = [0] * len(DID);
    MSN = [0] * len(DID);
    CEMS = [0] * len(DID);
    CEMN = [0] * len(DID);
    CESN = [0] * len(DID);
    CMSN = [0] * len(DID);
    EMSN = [0] * len(DID);
    CEMSN = [0] * len(DID);
    filter_list = [ "國",
                    "英",
                    "數",
                    "社",
                    "自",
                    "總",
                    "國英",
                    "國數",
                    "國社",
                    "國自",
                    "英數",
                    "英社",
                    "英自",
                    "數社",
                    "數自",
                    "社自",
                    "國英數",
                    "國英社",
                    "國英自",
                    "國數社",
                    "國數自",
                    "國社自",
                    "英數社",
                    "英數自",
                    "英社自",
                    "數社自",
                    "國英數社",
                    "國英數自",
                    "國英社自",
                    "國數社自",
                    "英數社自",
                    "國英數社自"];
    filter_dict = { "國" : C,
                    "英" : E,
                    "數" : M,
                    "社" : S,
                    "自" : N,
                    "國英" : CE,
                    "國數" : CM,
                    "國社" : CS,
                    "國自" : CN,
                    "英數" : EM,
                    "英社" : ES,
                    "英自" : EN,
                    "數社" : MS,
                    "數自" : MN,
                    "社自" : SN,
                    "國英數" : CEM,
                    "國英社" : CES,
                    "國英自" : CEN,
                    "國數社" : CMS,
                    "國數自" : CMN,
                    "國社自" : CSN,
                    "英數社" : EMS,
                    "英數自" : EMN,
                    "英社自" : ESN,
                    "數社自" : MSN,
                    "國英數社" : CEMS,
                    "國英數自" : CEMN,
                    "國英社自" : CESN,
                    "國數社自" : CMSN,
                    "英數社自" : EMSN,
                    "國英數社自" : CEMSN};
                   
    #將去年篩選結果轉換成31種組合                
    for i in range(len(filter_1)):
        if("-" in filter_1[i]):
            continue;
        for j in range(len(filter_list)-1, -1, -1):
            if((filter_1[i].find(filter_list[j])) >= 0):
                filter_dict[filter_list[j]][i] = re.findall("\d+", filter_1[i])[0];
                break;    
    for i in range(len(filter_2)):
        if("-" in filter_2[i]):
            continue;
        for j in range(len(filter_list)-1, -1, -1):
            if((filter_2[i].find(filter_list[j])) >= 0):
                filter_dict[filter_list[j]][i] = re.findall("\d+", filter_2[i])[0];
                break;    
    for i in range(len(filter_3)):
        if("-" in filter_3[i]):
            continue;
        for j in range(len(filter_list)-1, -1, -1):
            if((filter_3[i].find(filter_list[j])) >= 0):
                filter_dict[filter_list[j]][i] = re.findall("\d+", filter_3[i])[0];
                break;    
    for i in range(len(filter_4)):
        if("-" in filter_4[i]):
            continue;
        for j in range(len(filter_list)-1, -1, -1):
            if((filter_4[i].find(filter_list[j])) >= 0):
                filter_dict[filter_list[j]][i] = re.findall("\d+", filter_4[i])[0];
                break;    
    for i in range(len(filter_5)):
        if("-" in filter_5[i]):
            continue;
        for j in range(len(filter_list)-1, -1, -1):
            if((filter_5[i].find(filter_list[j])) >= 0):
                filter_dict[filter_list[j]][i] = re.findall("\d+", filter_5[i])[0];
                break;    
    UURL = [0] * len(DID);
    DURL = [0] * len(DID);
    Salary = [0] * len(DID);
    SalaryURL = [0] * len(DID);
    City = [0] * len(DID);
    PP = [0] * len(DID);
    result = {      "DID" : DID,
                    "UName" : UName,
                    "UURL" : UURL,
                    "DName" : DName,
                    "DURL" : DURL,
                    "Salary" : Salary,
                    "SalaryURL" : SalaryURL,
                    "TL1" : chinese,
                    "TL2" : english,
                    "TL3" : math,
                    "TL4" : social,
                    "TL5" : science,
                    "ELLEVEL" : ELLEVEL,
                    "C" : C,
                    "E" : E,
                    "M" : M,
                    "S" : S,
                    "N" : N,
                    "CE" : CE,
                    "CM" : CM,
                    "CS" : CS,
                    "CN" : CN,
                    "EM" : EM,
                    "ES" : ES,
                    "EN" : EN,
                    "MS" : MS,
                    "MN" : MN,
                    "SN" : SN,
                    "CEM" : CEM,
                    "CES" : CES,
                    "CEN" : CEN,
                    "CMS" : CMS,
                    "CMN" : CMN,
                    "CSN" : CSN,
                    "EMS" : EMS,
                    "EMN" : EMN,
                    "ESN" : ESN,
                    "MSN" : MSN,
                    "CEMS" : CEMS,
                    "CEMN" : CEMN,
                    "CESN" : CESN,
                    "CMSN" : CMSN,
                    "EMSN" : EMSN,
                    "CEMSN" : CEMSN,
                    "City": City,
                    "PP" : PP,
                    "Change" : Change,
                    "lastCriterion" : lastCriterion,
                    "rateOfThisYear" : rateOfThisYear,
                    "ExamURL" : ExamURL};
    result_df = pd.DataFrame(result);
    result_df.to_csv("OutputGsat.csv", encoding="utf_8_sig",index=False);
