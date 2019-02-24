import re
import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import urllib.parse
import sys
text_to_be_passed=sys.argv[1]
values={'q':text_to_be_passed}

data=urllib.parse.urlencode(values)
url='https://www.google.com/search?'+data


headers={}
headers['User-Agent']="Mozilla/5.0 (X11; Linux i686)"

request=urllib.request.Request(url,headers=headers)
response=urllib.request.urlopen(request)
response_data=response.read()

fhandler= open("sample.txt",'w')
list_of_urls=[]
list_to_be_write_into_the_file=[]
soup = BeautifulSoup(response_data, 'html.parser')
lst=soup.find_all("a")
string_to_be_matched=re.compile("http.*.pdf")
for urlinfetchedata in lst:
    url1=urlinfetchedata.get('href')
    lofurl=re.findall(string_to_be_matched, url1)
    for i in lofurl:
        list_of_urls.append(i)
for urls in list_of_urls:
    if(urls.find("webcache")!=-1):
        continue
    if (urls.find("google") != -1):
        continue
    if (urls.find("blogger") != -1):
        continue
    if (urls.find("youtube") != -1):
        continue
    position_of_plus=urls.find("+")
    if(position_of_plus==-1):
      list_to_be_write_into_the_file.append(urls)
    else:
        list_to_be_write_into_the_file.append(urls[:position_of_plus])

output = []
for urls in list_to_be_write_into_the_file:
    if urls not in output:
        output.append(urls)

for line in output:
    fhandler.write(line+"\n")

