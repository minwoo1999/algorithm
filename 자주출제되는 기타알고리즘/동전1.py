import math

N=int(input())

def is_prime_number(x):
    
    for i in range(2,int(math.sqrt(x))+1):
        
        if x%i==0:
            return False
        
    return True




count=0
inteval_sum=0
end=0

# start를 차례대로 증가시키며 반복

for start in range(n):
    print(inteval_sum)
    while inteval_sum<m and end<n: ##부분합 값이 m보다 작다면 end+=1 ,end 값은 n을 벗어나지않도록 함
        
        inteval_sum+=data[end]
        end+=1
        
    # 부분합이 m일 때 카운트 증가
    
    if inteval_sum==m:
        count+=1
    inteval_sum-=data[start] ## start 포인트를 증가시킨다, 즉 부분합에서 해당하는 스타트 data값을 빼주면된다.
    
    
print(count)