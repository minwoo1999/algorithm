## 시작점과 끝점이 첫번쨰 원소의 인덱스 0을 가리키도록한다.
## 현재 부분합이 M과 같다면 카운트하고
## 현재 부분합이 M보다 작다면 end 값을 1증가 
## 혅재 부분합이 M보다 크거나 같다면 start값을 1증가
## 모든경우를 확인할때까지 2번부터 4번까지의 과정을 반복한다.


n=5 # 데이터의 갯수
m=5 # 찾고하는 부분합 

data=[1,2,3,2,5] # 전체 수열

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