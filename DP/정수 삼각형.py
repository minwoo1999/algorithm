# 1932  정수 삼각형 (파이썬 Python)
n = int(input())
dp = []

for i in range(n):
    dp.append(list(map(int,input().split())))
    
    

for i in range(1,n):
    for j in range(0,i+1):
        
        if j==0:
            dp[i][0]+=dp[i-1][0] ## 0열끼리 더하기 현재 i층에서 i-1 층에있는 0열을 계속 더해감
            
        elif i==j: ## i==j는 마지막열에 있을시 그 전에있던 열을 계속 더해감
            dp[i][j]+=dp[i-1][j-1]
        else: 
            dp[i][j]+=max(dp[i-1][j-1],dp[i-1][j]) ## 두 수중 더 큰값을 더함

print(max(dp[n-1]))   