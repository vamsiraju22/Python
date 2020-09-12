import sys
import time
import os
import moviepy.video.io.ImageSequenceClip

local_time= time.localtime()
folder_name= time.strftime("%d-%m-%Y",local_time)

fps=1
choice= input("Do you want to create a new video with todays date? Press Y or y if yes else type whatever you want.")
if choice in ['Y', 'y']:
    folder_name= time.strftime("%d-%m-%Y",local_time)
    print(folder_name)
else:
    folder_name=input("If you want to create video on some other folder images, please enter the folder name in format DD-MM-YYYY eg 03-09-2020 \n")

for i in os.listdir(os.getcwd()):
    if folder_name not in os.listdir(os.getcwd()):
        print("You entered a folder that is not present. Please check!! Script is ending in 5 sec.")
        time.sleep(6)
        sys.exit()
print("Please wait.. Video is being created.")
path=os.getcwd()+'\\'+folder_name+'\\'
image_folder=path
image_files = [image_folder+'/'+img for img in os.listdir(image_folder) if img.endswith(".png")]
clip = moviepy.video.io.ImageSequenceClip.ImageSequenceClip(image_files, fps=fps)
clip.write_videofile('video on '+folder_name+'.mp4')
