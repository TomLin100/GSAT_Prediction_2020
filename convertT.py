import Tool
import pandas as pd
def convertt():
    inputFileName = ".26各科成績標準一覽表.xls";
    outputFileName = "T.xls";
    headers = ["TName", "Garde1", "Garde2", "Garde3", "Garde4", "Garde5"];
    subjects = ["國文", "英文", "數學", "自然", "社會" ];
    data = Tool.readExcel_T(inputFileName);
    
    inputData = [];
    garde1 = [];
    garde2 = [];
    garde3 = [];
    garde4 = [];
    garde5 = [];
#    print(data)
    for i in range(0, len(data), 5):
        inputData.append(data[i:i+5]);
    for i in range(len(inputData)):
        for j in range(len(inputData[i])):
            print(j)
            if j == 0:
                garde5.append(inputData[i][j]);
            if j == 1:
                garde4.append(inputData[i][j]);
            if j == 2:
                garde3.append(inputData[i][j]);
            if j == 3:
                garde2.append(inputData[i][j]);
            if j == 4:
                garde1.append(inputData[i][j]);
    inputData = [];
    inputData = [subjects, garde1, garde2, garde3, garde4, garde5];
    Tool.writeExcel(headers, outputFileName, inputData);
#    print(len(subjects))
#    print(len(garde1))
#    print(len(garde2))
#    print(len(garde3))
#    print(len(garde4))
#    print(len(garde5))
    df=pd.DataFrame({"TName":subjects,"Garde1":garde1,"Garde2":garde2,"Garde3":garde3,"Garde4":garde4,"Garde5":garde5})
    Tool.SaveDatabase(df,"T")

