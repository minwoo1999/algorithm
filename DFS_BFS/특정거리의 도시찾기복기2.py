from collections import deque

N,M,K,X=map(int,input().split())

graph=[[] for _ in range(N+1)]

for i in range(M):
    a,b=map(int,input().split())
    graph[a].append(b)
    

distance=[-1]*(M+1)
distance[X]=0

queue=deque()
queue.append(X)
while(queue):
    
    now=queue.popleft()
    
    
    for next_nod in graph[now]:
        
        if distance[next_nod]==-1:
            distance[next_nod]=distance[now]+1
            queue.append(next_nod)
            
check=False
for i in range(1,M+1):
    if distance[i]==K:
        print(i)
        check=True
        
if check==False:
    print(-1)
