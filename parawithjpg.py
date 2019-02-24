
import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE
fhand = open("sample.txt", 'r')
fhand1 = open("data.txt", 'w', encoding='utf8')
lst = []
for i in fhand:
    lst.append(i)

for url in lst:
        fhand1.write(
            "\n=========================================================================================================\n")
        fhand1.write('\n' + url + '\n')
        headers = {}
        headers['User-Agent'] = "Mozilla/5.0 (X11; Linux i686)"

        req = urllib.request.Request(url, headers=headers)
        resp = urllib.request.urlopen(req)
        resp_data = resp.read()
        soup = BeautifulSoup(resp_data, 'html.parser')
        lst1 = soup.find_all('img')
        for i in lst1:
                l=i.get("src")
                print(l)



