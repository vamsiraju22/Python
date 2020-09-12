import time
import pyautogui
import os
import cv2
from PIL import Image

named_tuple = time.localtime()
folder_name=time.strftime("%d-%m-%Y",named_tuple)
path=os.getcwd()+'\\'+folder_name+'\\'

print("To stop , just close")

print("SS are saved with timestamp as names")

try:
    os.makedirs(path)
    print("Folder created")
except:
    print("FOlder already present")
    pass

print(os.getcwd()+'\\'+folder_name+'\\')
path=os.getcwd()+'\\'+folder_name+'\\'

for i in range(0,3600):
    
    named_tuple = time.localtime()
    time_string=time.strftime("%m-%d-%Y %H.%M.%S",named_tuple)
    
    myScreenshot = pyautogui.screenshot()
    myScreenshot.save(path+time_string+'.png')
    print(time_string)
    time.sleep(1)
