import numpy as np
import cv2
import math  
import os
import xml.etree.ElementTree as ET
i=1
for filename in os.listdir("C:/python/rename_images/"): 
     filen=os.path.splitext(os.path.basename(filename))[0]
     print(filen)
     extension=os.path.splitext(os.path.basename(filename))[1]
     print(extension)
     if extension=='.jpg':
       img = cv2.imread("C:/python/rename_images/"+filen + ".jpg")
       cv2.imwrite("C:/python/rename_images/"+"W"+str(i)+ ".jpg",img)
       filen1=("W"+str(i))
       print(filen1)
       if filen!=filen1:
         os.remove("C:/python/rename_images/"+filen + ".jpg")
       i+=1
       