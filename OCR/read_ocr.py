#Reading characters from an image using OCR
pytesseract.tesseract_cmd = r'C:\Users\VK00489900\AppData\Local\Tesseract-OCR\tesseract.exe'

import pytesseract
from pytesseract import pytesseract
import PIL
from PIL import Image
import cv2
import csv

img = 'recalculate.png'
imge = Image.open(img)
data=pytesseract.image_to_boxes(imge)

#print(data)
count=0
final=""
for ind,i in enumerate(data):
    if count==0:
        print(data[0],end='')
        final+=data[0]
        count+=1
    try:
        if i =="\n":
            print(data[ind+1],end='')
            final+=data[ind+1]
    except:
        pass
    