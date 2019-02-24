import re
import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input("Enter url-")
html = urllib.request.urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, 'html.parser')
lst=soup.find_all("a",string=["PRINCIPAL&#039;S MESSAGE","Principal&#039;s Message","PRINCIPAL'S MESSAGE","Principal's Message","Principal","Principal Message"])

if(len(lst)!=0):
 for i in lst:
    s=i.get('href')

 url = url+s
 html = urllib.request.urlopen(url, context=ctx).read()
 soup1 = BeautifulSoup(html, 'html.parser')
 lst1=soup1.find_all('p')
 for j in lst1:
     if(j.string == None):
        continue
     print(j.string)
 print("=========================================================================================================")
else:
    fhand=open("obfuscatedhtml.txt",'w')
    fhand.write(soup.prettify())
    fhand.close()
    fhand=open("obfuscatedhtml.txt",'r')
    fhand1=open("html.txt",'w')
    for line in fhand:
        st1=line.split('%')
        for i in st1:
          if (len(i)==2):
            hex_str = i
            hex_int = int(hex_str, 16)
            new_int = hex_int + 0x00
            fhand1.write( chr(new_int))

    fhand1.close()
    fhand2=open("html.txt",'r')
    st=""
    for line in fhand2:
        st=st+line
    soup = BeautifulSoup(st, 'html.parser')

    lst=soup.find_all("p")

    for i in lst:
        print(i.string)
    
