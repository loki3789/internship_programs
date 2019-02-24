import re
import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl


ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE
fhand=open("sample.txt",'r')
fhand1=open("data.txt",'w',encoding='utf8')
fhand2=open("jpg_urls.txt",'w',encoding='utf8')
fhand3=open("jpg_names.txt",'w',encoding='utf8')
lst=[]
for i in fhand:
    lst.append(i)
    #print(i)
try:
    for l1 in lst:
            url = l1
            fhand1.write("\n=========================================================================================================\n")
            fhand1.write('\n'+url+'\n')
            headers = {}
            headers['User-Agent'] = "Mozilla/5.0 (X11; Linux i686)"

            req = urllib.request.Request(url, headers=headers)
            resp = urllib.request.urlopen(req)
            resp_data = resp.read()
            soup = BeautifulSoup(resp_data, 'html.parser')

            lst1 = soup.find_all('p')
            for data_in_p_tag in lst1:
                if (len(data_in_p_tag.text)<100):
                    continue

                fhand1.write(data_in_p_tag.text)
                break
            lst1 = soup.find_all('img')

            for link in lst1:
                url = link.get("src")


                if (url.endswith("jpg") and url.startswith("http")):
                    fhand2.write(url + '\n')
            lst1 = soup.find_all('h3')
            fhand1.write("Image name:")
            fhand1.write('   '+'"'+lst1[0].text+'.jpg'+'"')
            fhand3.write(lst1[0].text+'\n')


            fhand1.write("\n=========================================================================================================\n")
except:
    pass