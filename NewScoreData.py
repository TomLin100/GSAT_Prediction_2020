import Tool
import pandas as pd

def newscoredata():
    ename = [];
    score = [];

    inputFileName = ".22各科級分人數分布表.xls";
    outputFileName = "NewScoreData.csv";
    percentage = Tool.readExcel(inputFileName);
    ename = Tool.setEname("國文", 16, ename);
    ename = Tool.setEname("英文", 16, ename);
    ename = Tool.setEname("數學", 16, ename);
    ename = Tool.setEname("社會", 16, ename);
    ename = Tool.setEname("自然", 16, ename);
    for i in range(5):
        score = Tool.setScore(15, score);
    header = ["Ename", "Score", "Percentage"];
    inputData = [ename, score, percentage];
    Tool.writeExcel(header, outputFileName, inputData);
    df=pd.DataFrame({"Ename":ename,"Score":score,"Percentage":percentage})
    df.to_csv('NewScoreData.csv',encoding='utf-8-sig',index=False)
    Tool.SaveDatabase(df,"NewScoreData")