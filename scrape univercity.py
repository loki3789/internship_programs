import re
import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

usn = input("Enter usn-")
url="https://cbcs.fastvturesults.com/result/"
sem=input("Enter sem-")
slash='/'
url=url+usn+slash+sem
print(url)
html = urllib.request.urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, 'html.parser')
lst=soup.find_all("div",{"class":'col-3'})
for i in lst:
    print(i.find('Internal'))
