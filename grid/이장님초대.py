N=int(input())

t=list(map(int,input().split()))
t.sort(reverse=True)
for i in range(N):
    t[i]+=i


print(max(t)+2)