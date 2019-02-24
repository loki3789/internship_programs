import re
import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import urllib.parse
import sys
#text_to_be_passed=sys.argv[1]
text_to_be_passed = ''.join(sys.argv[1:])
values={'q':text_to_be_passed}
data=urllib.parse.urlencode(values)
offset=00
for i in range(0,10):
    stroffset=str(offset)
    url="https://www.google.co.in/search?"+data+"&client=opera&hs=Ngi&ei=E_taW6nEFdao9QOO_Lq4AQ&start="+stroffset+"&sa=N&biw=1205&bih=574"


    headers={}
    headers['User-Agent']="Mozilla/5.0 (X11; Linux i686)"

    request=urllib.request.Request(url,headers=headers)
    response=urllib.request.urlopen(request)
    response_data=response.read()

    fhandler= open("sample.txt",'a')
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

    for u in list_of_urls:
        if(u.find("webcache")!=-1):
            continue
        if (u.find("google") != -1):
            continue
        if (u.find("blogger") != -1):
            continue
        if (u.find("youtube") != -1):
            continue
        position_of_plus = u.find("+")
        if (position_of_plus == -1):
            list_to_be_write_into_the_file.append(u)
        else:
            list_to_be_write_into_the_file.append(u[:position_of_plus])

    output = []
    for urls in list_to_be_write_into_the_file:
        if urls not in output:
            output.append(urls)

    for line in output:
        fhandler.write(line + "\n")

    offset=offset+10


