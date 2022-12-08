from collections import deque
def dfs(V):
    
    dfs_visited[V]=1
    print(V,end=" ")
    for next_nod in graph[V]:
        if dfs_visited[next_nod]==0:
            dfs(next_nod)
            
            

def bfs():

    queue=deque()
    queue.append(V)
    bfs_visited[V]=1
    while(queue):
        now=queue.popleft()
        print(now,end=" ")
        for next_nod in graph[now]:
            if bfs_visited[next_nod]==0:
                bfs_visited[next_nod]=1
                queue.append(next_nod)
                    
    

N,M,V=map(int,input().split())

dfs_visited=[0]*(N+1)
bfs_visited=[0]*(N+1)
graph=[[] for _ in range(N+1)]
for i in range(M):
    a,b=map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)
    
for i in graph:
    i.sort()
    
    
dfs(V)
print()
bfs()