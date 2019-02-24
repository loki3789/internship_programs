fhand=open("sample.txt",'r')
fhand1=open("html.txt",'w')
for line in fhand:
    st1=line.split('%')
#print(st1)
    for i in st1:
        if (len(i)==2):
            hex_str = i
            hex_int = int(hex_str, 16)
            new_int = hex_int + 0x00
            fhand1.write( chr(new_int))

fhand1.close()
