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
lst1 = soup.find_all('p')
for data_in_p_tag in lst1:
    if (data_in_p_tag.text == None):
       continue

    print(data_in_p_tag.text)

    print("\n=========================================================================================================\n")