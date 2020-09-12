import re
import os
import time
lis=[]
path=input("Enter the path for which you want to find list of files:\n")
d=path
final=[]
for filename in os.listdir(d):
    try:
        final.append(filename[:-4])
    except:
        pass
text_file = open("List of Files.txt", "w")
print(final)
try:
    for i in final:
        text_file.write(str(i))
        text_file.write('\n')
except:
    print("Error in writing a file.")
text_file.close()
print("List of files Created Successfully")
time.sleep(5)
