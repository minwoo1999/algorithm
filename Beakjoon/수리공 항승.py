N,L=list(map(int,input("").split()))

position_list=list(map(int,input().split()))

position_list.sort()

repair=0
cnt=0
for i in position_list: ## 물이샌곳 하나씩 
    
    if repair<i:
        cnt+=1  ## 테이프의 갯수 
        repair=i+L-1 ## 물이 샌 위치+테이프의길이-1
        

print(cnt)