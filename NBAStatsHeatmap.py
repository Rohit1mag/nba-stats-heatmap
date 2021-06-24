import pandas as pd
import seaborn as sb
import matplotlib.pyplot as plt

pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)
pd.options.display.width = 0


def removeSpecialChars(df):
    for index, row in df.iterrows():
        try:
            print (row["Player"]) 
        except UnicodeEncodeError:
            df.drop(index, inplace = True)
    
    return df

def getDataList(df):
    columns = list(df)
    dataList = []
    for row in df.iterrows():
        rowList = []
        for name in columns:
            rowList.append(row[name])
        
        dataList.append(rowList)
    return dataList
        
        

#Main
#file = open("C:/Users/Rohi/Downloads/nba2020PerTable.csv", "w", encoding = "utf-8")
dataf = pd.read_csv("")#local file loc of data csv for that year
#dataf = removeSpecialChars(dataf)
#dataf.sort_values(by=['PER'], inplace=True, ascending=False)
#dataf.drop(dataf[dataf["G"] < 35].index, inplace = True)
dataf.drop(columns = ["Rk", "Player", "Pos", "Tm"], axis = 1, inplace = True)
#file.write(str(dataf))
#plt.figure(figsize = (16,10))
sb.heatmap(dataf.corr(), annot = True)
plt.show()


