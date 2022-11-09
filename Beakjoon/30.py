
num=list((input("")))
num.sort(reverse=True)
sum=0

for i in num:
    sum+=int(i)
    
  
if "0" not in num or sum%3!=0:
    print("-1")
else:
    print(''.join(num))
