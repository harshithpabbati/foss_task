from bs4 import BeautifulSoup
import requests
m=input("enter the name of the text file:")
file1=open(r"/home/harshith/Desktop/foss_tasks/"+m,"r")
a=file1.readline()
r=requests.get("http://www.google.com/search?btnG=1&q="+a)
data=r.text
soup=BeautifulSoup(data,"html.parser")
k=soup.select("h3")
m=soup.select("cite")
for i,j in zip(k,m):
	t=i.get_text()
	s=j.get_text()
	print(s)
	print(t)
