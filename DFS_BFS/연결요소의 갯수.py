def dfs(v):
    visited[v]=1

    for next_nod in graph[v]:
        if visited[next_nod]==0:
            visited[next_nod]=1
            dfs(next_nod)

N,M=map(int,input().split())




graph=[[] for _ in range(N+1)]

visited=[0]*(N+1)
for i in range(M):
    a,b=map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)
    
for i in graph:
    i.sort()




## 구현을 못한 부분
count=0
for i in range(1,N+1):
    if visited[i]==0:
        count+=1
        dfs(i)
        

print(count)