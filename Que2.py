
import requests
from bs4 import BeautifulSoup
import re

URL = "http://ful.io"
r= requests.get(URL)
htmlContent=r.content
#print(htmlContent)

soup=BeautifulSoup(htmlContent,'xmls.parser')
#print(soup.prettify)

t#itle=soup.title
#print(title)

gmail=re.findAll('\S+@\S+',soup)
phonenum=re.findAll('^\+?(44)?(0|7)\d{9,13}$',soup)

socialLinks=re.findAll('(?:https?:)?\/\/(?:www\.)?(?:facebook|fb)\.com\/(?P<profile>(?![A-z]+\.php)(?!marketplace|gaming|watch|me|messages|help|search|groups)[A-z0-9_\-\.]+)\/?',soup)

print(gmail)
print(phonenum)
print(socialLinks)




#1.command history
#2.ls -a
#3.from college time i m using linux so,i m very friendly/comfortable with linux
#and its with CUI(command user interface)

#4.apache tomcat for servlet application running
 #and SMTP for creating gmail automation script(or in general email sending)

