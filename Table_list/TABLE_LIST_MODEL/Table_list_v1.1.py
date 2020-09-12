# Python Script for Listing table  

# If you get any packge error , please install below package through command prompt
# pip install pandas
# 
# ---------------------------------------------------------- Program Start --------------------------------- 
import sys
print(sys.version)
import glob
import os
#import xlrd 
import re
import pandas as pd
import datetime

print("Execution Started")
start = datetime.datetime.now()
print("start_time",start)

currentDir=os.getcwd()       # getting current directory path
Source_path = os.path.join(currentDir,"Input\*")  # Source path to iterate all files
Target_folder = os.path.join(currentDir,"Output") # Target path to save the modified file  

Outputpath = "Output" + "\\"+"TABLE_LIST.xlsx"     # output path with corresponding file name
Target_path = os.path.join(currentDir,Outputpath)

writer = pd.ExcelWriter(Target_path, engine='xlsxwriter')

df1 = pd.DataFrame()  # Creating empty dataframe 
try:
 os.mkdir(Target_folder)   # Creating target folder if doesnt exist .
except:
 pass

print("List of Table Extarcted from Below ETL")
for x in glob.glob(Source_path):      # Iterating over files , such as .txt,.xml,.sql and any extension file
  file_name = os.path.split(x)    # spilt into (header,tail) ie. (path and lastname of path)
  ETL_NAME = re.sub(r'\.\w+',"",file_name[1])   # Extracting ETL_NAME
  #path_name = file_name[1].replace('.xml','new_name.xml') # to modify the filename
  #path_data = os.path.abspath(x)
  
# read the file and store it in variable 
  with open(x) as f:
   newText_df = f.read()
   
  list_table1 = re.findall(r'\$\$\w+\.\w+',newText_df) # TD table 
  list_table2 = re.findall(r'\$\$\w+\.\W+\w+',newText_df) # TD table 
  list_table1.extend(list_table2)
  list_table = list(dict.fromkeys(list_table1))
  #list_table = re.findall(r'\w+\.\w+',newText_df)
  #list_table = re.findall(r'\$\$\w+\.\$\$\w+\.\w+',newText_df)   # SF all table  
  set_table = set(list_table)   # removing duplicates
  x1 = [i.split(".") for i in set_table]     # creating list of dabasename and table name 
  df_set = pd.DataFrame(x1,columns = ["DBNAME","TABLE_NAME"])
  df_set.insert(0, "ETL_NAME",ETL_NAME, True)
  df1 = pd.concat([df1,df_set])
  print(ETL_NAME)
  

   
sheet1_name = "LIST_TABLES"
# write it in newfile and saving in target folder 
df1.to_excel(writer, sheet_name=sheet1_name,index = False)
writer.save()
print('Table list is written to target file ie Output folder')  

end = datetime.datetime.now()
print("end_time",end)
print(end - start)

# ------------------------------------------------- Thank You ---------------------------------------------
