import fake_useragent,requests
from bs4 import BeautifulSoup
import re

ua=fake_useragent.UserAgent()
count=0
# Downloading images from getty images.
for x in range(1,51):
	r=requests.get("https://www.gettyimages.co.uk/photos/mahendra-singh-dhoni?family=editorial&page="+str(x)+"&phrase=mahendra%20singh%20dhoni&sort=mostpopular",headers={"User-Agent":str(ua.chrome)})
	soup=BeautifulSoup(r.text,"html.parser")
	imgs=soup.find_all("img")
	for img in imgs:
		try:
			link=img["src"]
			if link.endswith("png"):
				continue
			img=requests.get(link)
			f=open("images/%s.jpg"%count,"wb")
			print("downloaded %s.jpg"%count)
			f.write(img.content)
			f.close()
			count+=1
		except:
			pass