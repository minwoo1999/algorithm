N,M,K=map(int,input().split())

array=list(map(int,input().split()))


array.sort()
array_max=array[N-1]
array_two_max=array[N-2]


result=[]
while(1):
    
    if M==0:
        break
    
    for i in range(K):
        result.append(array_max)
        M-=1
        
    result.append(array_two_max)
    M-=1
    
    
    
print(sum(result))
