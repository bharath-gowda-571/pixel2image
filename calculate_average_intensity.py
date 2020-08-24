#!/usr/bin/python3
import os
import cv2
from tqdm import tqdm
import json
file=open("intensities.txt","w")

dict_inten={}

for i in tqdm(range(len(os.listdir("resized_gray_images")))):
	img=cv2.imread("resized_gray_images/"+str(i)+".jpg",0)
	# calculating the average intensity of a greyscale image.
	average_intensity=int(round(sum(list(map(sum,img)))/10000))
	file.write((str(i)+".jpg").rjust(10)+"\t"+str(average_intensity).rjust(15)+"\n")
	
	try:
		dict_inten[average_intensity].append(str(i)+".jpg")
	except KeyError:
		dict_inten[average_intensity]=[str(i)+".jpg"]

file.close()

with open("intensities_dict.json","w") as json_file:
	json.dump(dict_inten,json_file)