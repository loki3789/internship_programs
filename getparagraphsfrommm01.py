import re
import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl


ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE
fhand=open("sample.txt",'r')
fhand1=open("data.txt",'a',encoding='utf8')
lst=[]
lst.append("http://www.art-and-archaeology.com/india/mamallapuram/mam01.html")


for url in lst:
        fhand1.write("\n=========================================================================================================\n")
        fhand1.write('\n'+url+'\n')
        headers = {}
        headers['User-Agent'] = "Mozilla/5.0 (X11; Linux i686)"

        req = urllib.request.Request(url, headers=headers)
        resp = urllib.request.urlopen(req)
        resp_data = resp.read()
        soup = BeautifulSoup(resp_data, 'html.parser')
        lst1 = soup.find_all('p')
        print(len(lst1))
        lst2 = soup.find_all('h3')
        for data_in_h_tag in lst2:
            fhand1.write(data_in_h_tag.text + '\n\n')

        for data_in_p_tag in lst1[0:2]:
            fhand1.write(data_in_p_tag.text + '\n\n')

