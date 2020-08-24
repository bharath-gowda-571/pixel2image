#!/usr/bin/python3

import os
import cv2
os.chdir("/home/bharath/Python/msDhoni_image")
os.mkdir("resized_gray_images")
# converting the images to 100x100 resolution and greyscale.
for i in os.listdir("images"):
	img=cv2.imread("images/"+i,0)
	print("resizing "+i)
	img=cv2.resize(img,(100,100),interpolation=cv2.INTER_CUBIC)
	cv2.imwrite("resized_gray_images/"+i,img)