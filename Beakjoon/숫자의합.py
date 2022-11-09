num=int(input(""))


list_num=list(map(str,input("").split()))
sum=0
for i in list_num:
    for j in i:
        sum+=int(j)
        
        
print(sum)