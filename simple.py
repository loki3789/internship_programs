import re
import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl
fhand=open("sample.txt",'w', encoding='utf8')


ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE
url=input("Enter-")
html = urllib.request.urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, 'html.parser')
lst1 = soup.find_all('div')
for data_in_p_tag in lst1:
        print(len(data_in_p_tag.text))
        if (len(data_in_p_tag.text)>100):
            str0=data_in_p_tag.text
            str1 = str0.replace("\t", "")
            print(str1)
            fhand.write(str1+"\n")
            fhand.write("====================================================================================================")
            lst=str1.split("\n")
            break
#fhand.write(str(len(soup.prettify())))
for i in  lst:
    if(len(i)>100):
        fhand.write(i+"\n")

fhand.close()


