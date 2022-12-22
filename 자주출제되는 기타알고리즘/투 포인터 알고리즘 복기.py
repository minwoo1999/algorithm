n=5 # 데이터의 갯수
m=5 # 찾고하는 부분합 

data=[1,2,3,2,5] # 전체 수열

count=0
inteval_sum=0
end=0

for start in range(n):
    
    while(inteval_sum<m and end<n):
        inteval_sum+=data[end]
        end+=1
    
    
    if inteval_sum==m:
        count+=1
    
    inteval_sum-=data[start]
    
print(count)