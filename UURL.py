from selenium import webdriver;
import pandas;

def uurl(url):
    #使用chrome的webdriver
    browser = webdriver.Chrome();
    
    #開啟網頁
#    browser.get("https://collego.ceec.edu.tw/Highschool/School");
    browser.get(url)
    
    elements_schoolUrls = browser.find_elements_by_xpath("//div[@id='box_collegeList']/div/a[@style='padding-right:5px;']");
    elements_schoolNames = browser.find_elements_by_xpath("//div[@id='box_collegeList']/div/a[@class='box__item']");
    
    schoolNames = [];
    schoolUrls = [];
    
    
    for i in range(len(elements_schoolUrls)):
        #print(elements_schoolNames[i].text, ":", elements_schoolUrls[i].get_property("href"));
        schoolNames.append(elements_schoolNames[i].text);
        schoolUrls.append(elements_schoolUrls[i].get_property("href"));
        
    
    csv_content = {"學校名稱" : schoolNames,
                   "學校網址" : schoolUrls};
    
    csv_content_df = pandas.DataFrame(csv_content);
    csv_content_df.to_csv("OutputUURL.csv", encoding="utf_8_sig");
    
    
    browser.close();
