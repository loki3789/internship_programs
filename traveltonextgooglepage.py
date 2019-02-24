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
    string_to_be_matched=re.compile("http.*")
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
        position=u.find("&")
        urlscont=u[:position]
        position1= urlscont.find("+")
        if(position1==-1):
            if(u[:position] not in list_to_be_write_into_the_file):
                list_to_be_write_into_the_file.append(u[:position])

        else:
            if (urlscont[:position] not in list_to_be_write_into_the_file):
                list_to_be_write_into_the_file.append(urlscont[:position1])

    output = []
    for x in list_to_be_write_into_the_file:
        if x not in output:
            output.append(x)

    for i in output:
        fhandler.write(i+"\n")

    offset=offset+10


