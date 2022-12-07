from collections import deque
N,M,K,X=map(int,input().split())

graph=[[] for _ in range(N+1)]

for _ in range(M):
    a,b=map(int,input().split())
    graph[a].append(b)
    
    
distance=[-1]*(N+1) # 방문하지않은 노드는 -1
distance[X]=0 # 출발 도시 0으로 설정

queue=deque()
queue.append(X)

while(queue):
    
    now=queue.popleft() # now에는 1이 담기고 queue빔
    
    # 현재 도시에서 이동할수있는 모든 도시 확인
    
    for next_nod in graph[now]:
        
        if distance[next_nod]==-1:
            
            #최단거리갱신
            #현재 도시와 출발도시 사이의거리 +=1
            distance[next_nod]=distance[now]+1
            queue.append(next_nod)
            
            
            
# 출발 도시로 부터의 최단거리가 K인 도시가 존재하지않느다면
#-1을 출력하기위해 check 변수를 False로 초기화

check=False

for i in range(1,N+1):
    # 도시들간의 최단거리를 확인하여 K와 동일하면 그 도시를 출력
    if distance[i]==K:
        print(i)
        
        check=True

if check==False:
    print("-1")