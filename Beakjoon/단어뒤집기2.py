


num=list(input())
i=0
while i < len(num):
    
    if num[i]=="<":
        i+=1
        
        while num[i]!=">":
            i+=1
            
        i+=1
    elif num[i].isalnum():
        start=i
        while i <len(num) and num[i].isalnum():
            i+=1
        tmp=num[start:i]
        tmp.reverse()
        num[start:i]=tmp
    
    else:
        i+=1
    
    
print(''.join(num))
            
