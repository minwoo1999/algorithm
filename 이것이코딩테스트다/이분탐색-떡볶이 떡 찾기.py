n,m=map(int,input().split())

array=list(map(int,input().split()))


start,end=0,max(array)
result=0
while(start<=end):
    total=0
    mid=(start+end)//2

    for i in array:
        if mid<i:
            total+=i-mid

    
    if total<m: ## 너무 많이짤랐어 좀 줄여
        end=mid-1
    else: ## 최소값,계속 찾기
        result=mid
        start=mid+1


print(result)