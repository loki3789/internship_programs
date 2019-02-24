import requests
index=0
fhand=open("sample.txt",'r')
for lines in fhand:
    file_url = lines.strip('\n')

    r = requests.get(file_url, stream=True)
    name=str(index)+".pdf"

    with open(name, "wb") as pdf:
        for chunk in r.iter_content(chunk_size=1024):

            # writing one chunk at a time to pdf file
            if chunk:
                pdf.write(chunk)
    print("completed")
    index=index+1