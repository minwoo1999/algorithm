def binary_search(array,target,start,end):
    
    while(start<=end):
        
        mid=(start+end)//2
        
        if array[mid]==target: ## 중값 인덱스의값이 target값과 같다면 return
            return mid
        elif array[mid]<target: ## target값이 더 크므로 시작값을 늘림
            start=mid+1
        elif target<array[mid]: ## target값이 더 작으므로 endpoint 하나씩 내림
            end=mid-1
    
    return "none" ## 아무런 값이 들어오지않았을 경우.
        
        


N=int(input())
array=list(map(int,input().split()))
array.sort()
M=int(input())
target=list(map(int,input().split()))


for i in target:
    result=binary_search(array,i,0,len(array))
    if result=="none":
        print("no",end=" ")
    else:
        print("yes",end=" ")