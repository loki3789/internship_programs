import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl
# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE
url = input('Enter - ')
html = urllib.request.urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, 'html.parser')
# Retrieve all of the anchor tagshttps://wordpress.com/post/intershipcom.wordpress.com/9
#soup = BeautifulSoup(page.content, 'html.parser')
lst=soup.find_all('p')
i1=[]
#print(soup.p.text)
for paraghraphs in lst:
    print(paraghraphs)
    print('\n\n')