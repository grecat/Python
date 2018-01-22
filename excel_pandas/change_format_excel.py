# -*- coding: utf-8 -*-
"""
THIS SCRIPT CHANGE STRUCTURE OF EXCEL SHEET
"""
import pandas as pd
from openpyxl import load_workbook

writer = pd.ExcelWriter("test.xlsx", engine='openpyxl')
book = load_workbook("test.xlsx")
writer.book = book
writer.sheets = dict((ws.title, ws) for ws in book.worksheets)
# READ EXCEL SHEET AS DATAFRAME
d2 = pd.read_excel("test.xlsx",sheetname = "Sheet2", index = 0, header =None)
#SPLIT DATAFRAME INTO PARTS
before =  d2.iloc[:4, :] # THIS PART STAY THE SAME
titles = d2.loc[4:4] # IN THIS PART "Topic" is changed to "Topics"
titles.loc[4:4, 4] = "Topics" # CHANGE OF EXCEL CELL "Topic" TO "Topics"
main = d2.iloc[5:7] #IN THIS PART IS ADDED A ROW IN EXCEL SHEET WITH ONLY ONE TOPIC
all_data =[] #HERE WILL BE STORED ROWS, THAT WILL BE ADDED TO NEW DATAFRAME
ending = d2.iloc[7:, :] #THIS PART STAY THE SAME
for row in range(5, 7): #ITERATE OVER ROWS IN DATAFRAME
    
    new_list = main.loc[row, 4].split(",")  #ALL TOPICS TO A LIST  
    some = main.loc[row:row] #ROW THAT WILL BE MODIFIED
    
    for topic in new_list: # ITERATE OVER TOPICS IN A LIST
        new_data = some        
        new_data.loc[row:row, 4] = topic.strip() #CELL CHANGED TO ONLY ONE TOPIC 
        h = new_data.copy() #COPY OF A ROW        
        all_data.append(h) #APPEND EACH ROW TO A LIST
        
all_ser = pd.concat(all_data, ignore_index = True)   # PUT ALL ROWS TO DATAFRAME
tofinish = pd.concat([before,titles, all_ser, ending], ignore_index = True) #WRITE ALL PARTS TO ONE DATAFRAME

#WRITE MODIFIED DATAFRAME TO EXCEL SHEET
tofinish.to_excel(writer, sheet_name='Sheet2', header=None, index=False)
writer.save()
