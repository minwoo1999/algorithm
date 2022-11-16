n,m,k=map(int,input().split())


array=list(map(int,input().split()))
    
array.sort()
array_max=array[n-1]
array_max2=array[n-2]
result=0
while(1):
    
    for i in range(k):
        if m==0:
            break
        result+=array[n-1]
        m-=1
    
    if m==0:
        break

    result+=array[n-2]
    m-=1
    
print(result)
    