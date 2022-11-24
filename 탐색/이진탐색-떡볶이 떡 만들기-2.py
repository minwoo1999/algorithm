N,M=map(int,input().split())

meal=list(map(int,input().split()))


start=0
end=max(meal)

while(start<=end):

    total=0    
    mid=(start+end)//2
    
    for i in range(len(meal)):
        if mid<meal[i]:
           total+=meal[i]-mid
           
    if total<M:
        end=mid-1
    else:
        result=mid
        start=mid+1
        
print(result)