#!/usr/bin/python3
import json
import cv2
import numpy
import random
from tqdm import tqdm

# When the intensity doesnt exist in the dictionary.
def closest(lst, K):       
    return lst[min(range(len(lst)), key = lambda i: abs(lst[i]-K))] 

# Image which we are converting
img=cv2.imread("msd6.jpeg",0)

height,width=img.shape[:2]
print(height,width)

# Resizing the image while still maintaining the aspect ratio.
aspect_ratio=height/width
new_height,new_width=125,int(125/aspect_ratio)
print(new_height,new_width)
img=cv2.resize(img,(new_width,new_height),interpolation=cv2.INTER_CUBIC)

# Creating a blank image to be rendered
final_img=numpy.zeros((new_height*100,new_width*100),numpy.uint8)


# loading the image based on their intensities.
with open("intensities_dict.json","r") as file:
	dict_inten=json.load(file)

inten_lst=list(map(int,list(dict_inten.keys())))
print(inten_lst)

# acessing each pixel and rendering the image.
for i in tqdm(range(new_height)):
	for j in range(new_width):
		val=img[i][j]
		try:
			temp_img=cv2.imread("resized_gray_images/"+random.choice(dict_inten[str(val)]),0)
			final_img[i*100:(i+1)*100,j*100:(j+1)*100]=temp_img
		except KeyError:
			temp_img=cv2.imread("resized_gray_images/"+random.choice(dict_inten[str(closest(inten_lst,val))]),0)
			final_img[i*100:(i+1)*100,j*100:(j+1)*100]=temp_img
print(final_img.shape[:2])

# writing the final image
cv2.imwrite("rendered_image7.jpg",final_img)