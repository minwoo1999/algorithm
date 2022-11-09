computer=int(input(""))
ssang=int(input(""))
result=[]
temp=1
for i in range(ssang):
    a=list(map(int,input("").split()))

    if 1 in a:
        result.append(a[0])
        result.append(a[1])
        
        if 1!=a[0]:
            temp=a[0]
        else:
            temp=1
        if 1!=a[1]:
            temp=a[1]
        else:
            temp=1
                
    if temp in a:
        result.append(a[0])
        result.append(a[1])
        

z=set(result)
if 1 in z:
    z.remove(1)
    print(len(z))
else:
    print(len(z))
    