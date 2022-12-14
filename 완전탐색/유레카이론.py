from itertools import product

K=int(input())


for i in range(K):
    eureka=[]
    result=[]
    num=0
    n=int(input())

    i=1

    while(1):
    
        num=i*(i+1)//2
        result.append(num)
        
        if n<=num:
            break
        
        i+=1
        
    result=list(product(result,repeat=3))
    
    for i in result:
        if sum(i)==n:
            eureka.append(1)
            break
    
    if len(eureka)==0:
        print(0)
    else:
        print(1)
    
    
        
    

        
        