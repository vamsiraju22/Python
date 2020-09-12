import os
import time
path=input("Enter the path for which you want to find list of files:\n")
a=path
result=""
total_list = []
for filename in os.listdir(a):
    f = open(os.path.join(a, filename), "r")
    searchlines = f.readlines()
    
    line_list = []
    for line in (searchlines):
        total_list.append(line)
    total_list.append("--=======================================")

    def listToString(s):
        str1 = " "
        return (str1.join(s))


    SQL = listToString(total_list)
    result = result + '\n' + "--=================================================================================="
    result= result+SQL


text_file = open("Merged Output File.txt", "w")
try:
    for i in total_list:
        text_file.write(i)
        text_file.write('\n')
except:
    print("Error in writing a file.")
text_file.close()
print("The files are merged successfully.")
time.sleep(5)
