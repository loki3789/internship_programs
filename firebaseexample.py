from firebase import firebase
import re
import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE
url = input('Enter - ')
html = urllib.request.urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, 'html.parser')

lst=soup.find_all('table', attrs={ "class":"indx"})

l=[]
count=0
for i in lst:
    
    i1=i.find_all('a',limit=20)
    for g in i1:
        if(count<20):
          s=url+'/'+g.get('href')
          count+=1
          l.append(s)
#print(l)
url=l[0]
textofscrape=''
html = urllib.request.urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, 'html.parser')
lst=soup.find_all('p')
for v in lst:
    textofscrape+=v.text
firebase=firebase.FirebaseApplication('https://sample-ce36e.firebaseio.com/')
result=firebase.put('','sample',textofscrape)
