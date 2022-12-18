N=int(input())
step=[]
for i in range(N):
    step.append(int(input()))

dp=[0]*N


if len(step)<=2:
    print(sum(step))
else:

    dp[0]=step[0] #첫번째 계단의 최댓값
    dp[1]=step[0]+step[1] #두번째 계단의 최대값
    dp[2]=max(step[0]+step[2],step[1]+step[2])

    for i in range(3,N):
        dp[i]=max(dp[i-3]+step[i-1]+step[i],dp[i-2]+step[i])

    print(dp[-1])