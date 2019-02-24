import re
import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl
import requests

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE
fhand=open("sample.txt",'r')
fhand1=open("data.txt",'w',encoding='utf8')
lst=[]

for i in fhand:
    lst.append(i)

i=0
for url in lst:

        headers = {}
        headers['User-Agent'] = "Mozilla/5.0 (X11; Linux i686)"

        req = urllib.request.Request(url, headers=headers)
        resp = urllib.request.urlopen(req)
        resp_data = resp.read()
        soup = BeautifulSoup(resp_data, 'html.parser')
        lst1 = soup.find_all('img')

        for link in lst1:
            url=link.get("src")

            if(url.endswith("jpg") and url.startswith("http")):
                fhand1.write(url+'\n')
