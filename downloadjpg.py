import requests
lst=open("jpg_urls.txt",'r')
l=[]
for line in lst:
    u=line.find('\n')
    l.append(line[:u])
i=0
lst=open("jpg_names.txt",'r')
lnames=[]
for line in lst:
    u=line.find('\n')
    lnames.append(line[:u])

for url in l:
        name=lnames[i]+'.jpg'
        print(name)
        print(url)
        f = open(name,'wb')
        f.write(requests.get(url).content)
        f.close()
        i=i+1
