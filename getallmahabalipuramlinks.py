import re
import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl
fhand=open("sample.txt",'a')
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE
url = "https://www.mahabalipuram.co.in"
html = urllib.request.urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, 'html.parser')

lst = soup.find_all('td')
l = []
count = 0
for i in lst:
    i1 = i.find_all('a')
    for g in i1:
        if (count < 20):
            l.append(g.get('href'))

for urll in l[:11]:
    fhand.write(url+'/'+urll+'\n')