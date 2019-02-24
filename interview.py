n=str(input("enter number:"))
j=len(n)
n=int(n)
r=[]
for i in range(0,j):
        rem=n%16
        n=n//16
        r.append(rem)
print(r)     
    
