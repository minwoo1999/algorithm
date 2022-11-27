## 너비우선탐색 가까운 노드부터 우선적으로 탐색하는 알고리즘
## BFS는 큐 자료구조를용한다.

## 1.탐색 시작노드를 큐에 삽입하고 방문처리를 한다.
## 2.큐에서ㅗ 노드를 꺼낸 뒤 해당 노드의 인접노드중에서 방문하지않은
##노드를 모두 큐에 삽입하고 방문처리한다.
## 3.2번의 과정이 수행할수없을때ㅣ까지 반복 

from collections import deque

def bfs(graph,start,visited):
    queue=deque([start])
    visited[start]=True
    while queue:
        print(queue)
        v=queue.popleft()
        
        print(v,end=" ")
        
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i]=True




## 각 노드가 연결된 정보를 표현(2차원 리스트)
graph=[
    [],
    [2,3,8],
    [1,7],
    [1,4,5],
    [3,5],
    [3,4],
    [7],
    [2,6,8],
    [1,7]
    
       ]

# 각 노드가 방문된 정보를 표현(1차원 리스트)
visited=[False]*9

bfs(graph,1,visited)
