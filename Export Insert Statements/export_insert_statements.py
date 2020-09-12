import teradata as teradata
import pandas as pd
import getpass
import sys
from tqdm import tqdm
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
    session= udaExec.connect(method="odbc", system="TDTEST", username=b, password=c, driver="Teradata",authentication='LDAP');
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


import os
def get_query():
    d=os.getcwd()
    for filename in os.listdir(d):
        if filename in ("query.txt"):
            f = open(os.path.join(d, filename), "r")
            searchlines = f.readlines()
            total_list = []
            for line in (searchlines):
                total_list.append(line)
            
    
            def listToString(s):
                str1 = " "
                return (str1.join(s))
            query1 = listToString(total_list)
    f.close()
    return(query1)
query1 = get_query()

query2 = """
sel * from etlvwdb.dw_job_groups where job_group_id in (
 select distinct job_group_id from etlvwdb.dw_job_streams where job_stream_id in ( 'wf_N_SALES_HIER_VER_CNFRMD',
'wf_N_SALES_TERRITORY_ASSGN_CNF_TV'))"""

Exec_start_Time=time.time();
try:
    print("Please wait... Connection is getting Established.")
    df = pd.read_sql(query1,connection)
except:
    print("Error in executing the query. Please verify !!! ");
    time.sleep(5)
    sys.exit()
Exec_End_Time=time.time()
print("Your query is executed.")

Total_Exec_Time=Exec_End_Time-Exec_start_Time
print("\n\nTotal Time Taken execute the query and load into dataframe: %f secs"%Total_Exec_Time);
def insert_func(df):
    df=df.fillna('NULL')
    l=[]
    s=""
    value_list=[]
    count=range(0,df.shape[0])
    for ind in tqdm(count):
            
        for i,j in df.items():
            #print(j[0])
            val=j[ind]
            if val is not None:
                try:
                    val=val.strip()
                except:
                    try:
                        val=val.strftime("%Y-%m-%d %H:%M:%S")
                    except:
                        pass
            l.append(val)
        s=""
        st=""
        for i in l:
            if i is not None:
                if i is 'NULL':
                    s=s+"NULL"+","
                else:
                    i=str(i)
                    s=s+"'"+i+"',"
        st="("+s[:-1]+")"
        
        string_value=""
        for i,j in df.items():
            string_value=string_value+i+','
        value="insert into etlvwdb_ts1.dw_job_streams("+string_value[:-1]+") values"+st+";"+"-"*100
        value_list.append(value)
        l=[]
        s=""
        #print("--"*50)
    return(value_list)

if df.shape[0]!=0:
    print("Insert Statements preparation started.")
    final=insert_func(df)
    print("Insert statements prepared. File being created")
    text_file = open("Insert_statements.txt", "w")
else:
    print("Error!!! Please Check the query and database you selected")
    time.sleep(5)
    sys.exit()
try:
    for i in final:
        text_file.write(str(i))
        text_file.write('\n')
except:
    print("Error in writing a file.")
text_file.close()
connection.close()
print("Successfully created the file!!")
time.sleep(10)
