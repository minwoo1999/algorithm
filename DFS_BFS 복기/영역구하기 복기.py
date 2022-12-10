from collections import deque

def bfs(x,y):
    global areas
    visited[x][y]=1
    area=1
    q=deque()
    q.append((x,y))
    
    while(q):
        x,y=q.popleft()
        
        dx=[-1,1,0,0]
        dy=[0,0,-1,1]
        
        for i in range(4):
            
            nx=x+dx[i]
            ny=y+dy[i]
            
            if -1<nx<M and -1<ny<N:
                
                if board[nx][ny]==0 and not visited[nx][ny]:
                    visited[nx][ny]=1
                    q.append((nx,ny))
                    area+=1
       
    
    areas.append(area)             
                    
                            
        
        
        


M,N,K=map(int,input().split())

board=[[0]*N for i in range(M)]
visited=[[0]*N for i in range(M)]

areas=[]

for i in range(K):
    x1,y1,x2,y2=map(int,input().split())
    
    for i in range(y1,y2):
        for j in range(x1,x2):
            board[i][j]=1
            
            

for i in range(M):
    for j in range(N):
        
        if board[i][j]==0 and not visited[i][j]:
            bfs(i,j)
            
            
areas.sort()
print(len(areas)) 
for i in areas:
    print(i,end=" ")