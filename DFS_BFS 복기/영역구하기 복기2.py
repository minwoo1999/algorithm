from collections import deque

def bfs(x,y):
    
    # 전역변수 선언
    global areas
    ## 방문처리
    visitied[x][y]=1
    
    queue=deque()
    queue.append((x,y))
    area=1
    
    while(queue):
        
        x,y=queue.popleft()
        
        # 상하좌우
        dx=[-1,1,0,0]
        dy=[0,0,-1,1]
        for i in range(4):
            
            ##상하좌우로 표시
            nx=x+dx[i]
            ny=y+dy[i]
            ##영역안에 있을시
            if -1<nx<M and -1< ny<N:
                
                if graph[nx][ny]==0 and visitied[nx][ny]==0:
                    ##방문처리
                    visitied[nx][ny]=1
                    queue.append((nx,ny))
                    area+=1
                    
    
    areas.append(area)

## 세로 가로 영역값 입력

M,N,K=map(int,input().split())

## 2차원배열 및 방문처리를 위한 2차원배열 생성
graph=[[0]*N for _ in range(M)]
visitied=[[0]*N for _ in range(M)]


## 색칠되어있는 부분은 찾아서 1로 표시
for i in range(K):
    x1,y1,x2,y2=map(int,input().split())
    
    for i in range(y1,y2):
        for j in range(x1,x2):
            graph[i][j]=1
            
areas=[]
## 해당하는 직사각형이 0이고 방문을 하지않았다면 bfs로 넓이우선탐색 시작            
for i in range(M):
    for j in range(N):
        
        if graph[i][j]==0 and not visitied[i][j]:
            bfs(i,j)
                
## 정렬
areas.sort()
## 길이출력
print(len(areas))

for i in areas:
    print(i, end=" ")