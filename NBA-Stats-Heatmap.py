from tkinter import *
import pandas as pd
import seaborn as sb
import matplotlib.pyplot as plt
import sys

def makeMap():
    drops=[]
    for cat in categories:
        if categories[cat].get()==0:
            drops.append(cat)
    dataf.drop(columns=drops, axis=1, inplace=True)
    sb.heatmap(dataf.corr(), annot = True)
    plt.show()
    
root=Tk()

dataf=pd.read_csv("nba2020Advanced.csv")
dataf.drop(columns = ["Rk", "Player", "Pos", "Tm", "Age", "G", "MP", "WS/48", "FTr"], axis = 1, inplace = True) #Dropping
categories={"PER": IntVar(), "TS%": IntVar(), "3PAr": IntVar(), "ORB%": IntVar(), "DRB%": IntVar(), "TRB%": IntVar(), "AST%": IntVar(), "STL%": IntVar(), "BLK%": IntVar(), "TOV%": IntVar(), "USG%": IntVar(), "OWS": IntVar(), "DWS": IntVar(), "WS": IntVar(), "OBPM": IntVar(), "DBPM": IntVar(), "BPM": IntVar(), "VORP": IntVar()} 
    
Label(root, text="Choose the categories you want to see in the heatmap: ").grid(row=0, sticky=W)

Checkbutton(root, text="PER", variable=categories["PER"]).grid(row=1, sticky=W)
Checkbutton(root, text="TS%", variable=categories["TS%"]).grid(row=2, sticky=W)
Checkbutton(root, text="3PAr", variable=categories["3PAr"]).grid(row=3, sticky=W)
Checkbutton(root, text="ORB%", variable=categories["ORB%"]).grid(row=4, sticky=W)
Checkbutton(root, text="DRB%", variable=categories["DRB%"]).grid(row=5, sticky=W)
Checkbutton(root, text="TRB%", variable=categories["TRB%"]).grid(row=6, sticky=W)
Checkbutton(root, text="AST%", variable=categories["AST%"]).grid(row=7, sticky=W)
Checkbutton(root, text="STL%", variable=categories["STL%"]).grid(row=8, sticky=W)
Checkbutton(root, text="BLK%", variable=categories["BLK%"]).grid(row=9, sticky=W)
Checkbutton(root, text="TOV%", variable=categories["TOV%"]).grid(row=10, sticky=W)
Checkbutton(root, text="USG%", variable=categories["USG%"]).grid(row=11, sticky=W)
Checkbutton(root, text="OWS", variable=categories["OWS"]).grid(row=12, sticky=W)
Checkbutton(root, text="DWS", variable=categories["DWS"]).grid(row=13, sticky=W)
Checkbutton(root, text="WS", variable=categories["WS"]).grid(row=14, sticky=W)
Checkbutton(root, text="OBPM", variable=categories["OBPM"]).grid(row=15, sticky=W)
Checkbutton(root, text="DBPM", variable=categories["DBPM"]).grid(row=16, sticky=W)
Checkbutton(root, text="BPM", variable=categories["BPM"]).grid(row=17, sticky=W)
Checkbutton(root, text="VORP", variable=categories["VORP"]).grid(row=18, sticky=W)

Button(root, text="Submit", command=makeMap).grid(row=19, sticky=W)



root.mainloop()


