def binary_search(first,end,array,mid,M):
    
    
    sum=0
    
    mid=(first+end)//2
    
    for i in range(len(array)):
        
        if mid<array[i]:
            sum+=array[i]-mid
    
    
    if M==sum:
        return mid
    elif M<sum:
        return binary_search(mid+1,end,array,(mid+end)//2,M)
    else:
        return binary_search(first,mid-1,array,(mid+end)//2,M)



N,M=map(int,input().split())

meal=list(map(int,input().split()))

mid=1+max(meal)
print(binary_search(0,max(meal),meal,mid,M))
