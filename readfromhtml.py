import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
fhand=open("html.txt",'r')
st=""
for line in fhand:
    st=st+line
soup = BeautifulSoup(st, 'html.parser')

lst=soup.find_all("p")
#table=soup.find("table","alternate1")
#lst=table.find("tr",attrs={ "class":"alternate1"})
for i in lst:
    print(i.string)
