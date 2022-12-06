N=input()

alpha=[]
number=[]
sum=0
for i in N:
    if i.isalpha():
        alpha.append(i)
    else:
        number.append(i)
        

alpha.sort()
for i in number:
    sum+=int(i)
    

alpha.append(str(sum))
print(''.join(alpha))

