num=int(input())

s=[300,60,10]
    
if num %10!=0:

    print(-1)
else:
    a=b=c=0
    a=num//s[0]
    b=num%s[0]//s[1]
    c=num%s[0]%s[1]//s[2]
        
    print(a,b,c)
    
    
    
