import re
import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl
#fhand=open("sample.txt",'w')
# Ignore SSL certificate errors

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE
listofurls=["http://www.sapthagiri.edu.in/","http://www.msec.ac.in/","http://bit-bangalore.edu.in/","http://ksit.ac.in/","https://bmsit.ac.in/"]
for l1 in listofurls:
 url = l1
 html = urllib.request.urlopen(url, context=ctx).read()
 soup = BeautifulSoup(html, 'html.parser')
 lst=soup.find_all("a",string=["PRINCIPAL&#039;S MESSAGE","Principal&#039;s Message","PRINCIPAL'S MESSAGE","Principal's Message","Principal","Principal Message"])
 #print(lst)

 for i in lst:
    s=i.get('href')
    
 #print(s)

 url = url+s
 #print(url)
 html = urllib.request.urlopen(url, context=ctx).read()
 soup1 = BeautifulSoup(html, 'html.parser')
 lst1=soup1.find_all('p')
 for j in lst1:
     if(j.string == None):
        continue
    
     print(j.string)
 print("=========================================================================================================")
