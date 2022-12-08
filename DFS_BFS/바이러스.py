def dfs(v):
    visitied[v]=1
    
    for next_nod in graph[v]:
        if visitied[next_nod]==0:
            dfs(next_nod)

n=int(input())
v=int(input())

graph=[[] for _ in range(n+1)]
visitied=[0]*(n+1)
for i in range(v):
    a,b=map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)
    
    
dfs(1)

print(sum(visitied)-1)


    