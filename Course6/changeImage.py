#!/usr/bin/env python3

from PIL import Image
#from resizeimage  import resizeimage
import os
home="/home/student-00-f3438403c3f4/supplier-data/images/"
os.chdir(home)
arr = [f for f in os.listdir('.') if f.endswith('.tiff')]
print(arr)
for images in arr:
    #print(os.path.basename(images))
    img = Image.open(images).convert('RGB')
    #img=img.rotate(90)
    img=img.resize((600,400))
    img_format="jpeg"
    img.save(images[:-5]+".jpeg")
