from selenium import webdriver;
from time import sleep;
import pandas;
import time
def durl():
    
    finalDepartmentUrls = [];    #科系官方網站的網址list(最後要擷取的網址)
    departmentNames = [];    #科系名稱list
    
    browser = webdriver.Chrome();
    start = time.time()
    #擷取學校名稱
    browser.get("https://collego.ceec.edu.tw/Highschool/School"); 
#    browser.get(url);    #開啟全部大學網頁
    elements_schoolNames = browser.find_elements_by_xpath("//div[@id='box_collegeList']/div/a[@class='box__item']");    #擷取含有學校名稱的元素
    
    schoolNames = [];    #學校名稱List
    for i in range(len(elements_schoolNames)):    #將元素中的學校名稱取出存入list
        schoolNames.append(elements_schoolNames[i].text);
    
    print(schoolNames)
    #擷取科系名稱和科系網頁
    for schoolName in schoolNames:
        url = "https://collego.ceec.edu.tw/Login/Search?t=" + schoolName;
        browser.get(url);
        sleep(2);    #初次進入學系網頁會自動滾動至下方搜尋結果，暫停一下讓網頁讀取
        
        scrollHeight = 0;
        scrollHeightNext = 1;
        while scrollHeight < scrollHeightNext:    #學系網頁為瀑布網頁，需滾動至最下方才能取得完整內容。
            scrollHeight = browser.execute_script("return document.body.scrollHeight");
            browser.execute_script("window.scrollTo(0, document.body.scrollHeight);");
            sleep(1);
            scrollHeightNext = browser.execute_script("return document.body.scrollHeight");
        
        elements_department = browser.find_elements_by_xpath("//div[@class='scard well well-add-card']/a");    #擷取含有科系名稱和網址的元素
        
        departmentUrls = [];    #科系網址list(此科系網址並非該科系官方網站)
        for i in range(len(elements_department)):
            if "DepartmentIntro" in elements_department[i].get_property("href"):
                departmentNames.append(elements_department[i].text);
                departmentUrls.append(elements_department[i].get_property("href"));
        
        for departmentUrl in departmentUrls: 
            url = departmentUrl;
            browser.get(url);
            elements_finalDepartmentUrl = browser.find_elements_by_xpath("//a[@style='padding-left:15px;']");    #擷取含有科系官方網站網址的元素
            departmentUrlcurrentCount = len(finalDepartmentUrls);    #紀錄目前的科系官方網站數量，若該科系網站沒有找到該科系官方網站網址就填入0
            for i in range(len(elements_finalDepartmentUrl)):    #從科系網站找出的url中過濾出科系官方網站網址
                if ".edu.tw" in elements_finalDepartmentUrl[i].get_property("href"):
                    finalDepartmentUrls.append(elements_finalDepartmentUrl[i].get_property("href"));
            
            if departmentUrlcurrentCount == len(finalDepartmentUrls):    #若該科系網站沒有找到該科系官方網站網址就填入0
                finalDepartmentUrls.append("0");
            
    browser.close();
    
    csv_content = {"科系名稱" : departmentNames,
                   "科系網址" : finalDepartmentUrls};
    
    csv_content_df = pandas.DataFrame(csv_content);
    csv_content_df.to_csv("OutputDURL.csv", encoding="utf_8_sig");

    end = time.time()
    running_time = end-start
    print('科系網址 time cost : %.5f sec' %running_time)