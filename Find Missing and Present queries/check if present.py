import teradata as teradata
import pandas as pd
import getpass
import sys
from tqdm import tqdm 
import os
import time

print('Enter details for Teradata connection')
b = input("User ID:")
c = getpass.getpass()


def Teradata_Dev_Conn() :
 # TeraData Connection... 
    udaExec = teradata.UdaExec()  # keep udaexec.ini configuration file in the same directory of python script    
    session= udaExec.connect(method="odbc", system="TDDEV", username=b, password=c, driver="Teradata",authentication='LDAP');
    return session
 
def Teradata_Prod_Conn() :
 # TeraData Connection... 
    udaExec = teradata.UdaExec()  # keep udaexec.ini configuration file in the same directory of python script    
    session= udaExec.connect(method="odbc", system="TDPROD", username=b, password=c, driver="Teradata",authentication='LDAP');
    return session

def Teradata_Stage_Conn() :
 # TeraData Connection... 
    udaExec = teradata.UdaExec()  # keep udaexec.ini configuration file in the same directory of python script    
    session= udaExec.connect(method="odbc", system="TDPROD", username=b, password=c, driver="Teradata",authentication='LDAP');
    return session
choice = input("Enter to which database you would want to connect.(Choose among 1,2,3)\nMake sure your query has correct database name.\n Prod -->  1\n Stage -->  2\n Dev -->  3\n")

if choice=='1':
    connection=Teradata_Prod_Conn()
elif choice=='2':
    connection=Teradata_Stage_Conn()
elif choice=='3':
    connection=Teradata_Dev_Conn()
else:
    print("Invalid Choice.")
    sys.exit()

def check_stats(query,connection):
    query2 = query
    td_con=connection
    present=""
    not_present=""
    with td_con.cursor () as cur:
        try:
            cur.execute (query2)
            row = cur.fetchall ()
            present=(query2)
        except:
            #print("No stats",query2)
            not_present=(query2)
        return(present,not_present)
def get_stats_query():
    d=os.getcwd()
    for filename in os.listdir(d):
        if filename in ("query.txt"):
            f = open(os.path.join(d, filename), "r")
            searchlines = f.readlines()
            total_list = []
            line_list = []
            for line in (searchlines):
                total_list.append(line)
            
    
            def listToString(s):
                str1 = " "
                return (str1.join(s))
            query1 = listToString(total_list)
    f.close()
    return(total_list)
complete_list=get_stats_query()
stats_present=[]
stats_not_present=[]
print("Please wait.. Fetching the query results.")
count=1
print("Fetched queries: ",end='')
for i in (complete_list):
    p,n=check_stats(i,connection)
    stats_present.append(p)
    stats_not_present.append(n)
    print(count,end=' ')
    print(",",end='')
    count+=1
print(len(stats_present),len(stats_not_present))
text_file1 = open("Statements that are present.txt", "w")
try:
    for i in stats_present:
        if len(i)>10:
            text_file1.write(str(i))
            text_file1.write('\n')
    print("File for those statements that are present is created.")
except:
    print("Error in writing a file.")
text_file1.close()
text_file2 = open("Statements that are missing.txt", "w")
try:
    for i in stats_not_present:
        text_file2.write(str(i))
        text_file2.write('\n')
    print("File for those statements that are not present is created.")
except:
    print("Error in writing a file.")
text_file2.close()
connection.close()
time.sleep(5)
