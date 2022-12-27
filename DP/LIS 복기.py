n=int(input())
array=list(map(int,input().split()))

DP=[1]*n

for i in range(n):
    for j in range(i):
        if array[j]<array[i]:
            DP[i]=max(DP[i],DP[j]+1)
            
result=max(DP)
print(result)