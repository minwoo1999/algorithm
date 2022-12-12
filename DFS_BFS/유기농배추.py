from collections import deque

def bfs(x,y):
    visitied[x][y]=1
    
    
    queue=deque()
    queue.append((x,y))
    
    while(queue):
        
        x,y=queue.popleft()
        
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            
            if -1<nx<N and -1 <ny<M:
                
                if graph[nx][ny]==1 and visitied[nx][ny]==0:
                    visitied[nx][ny]=1 
                    queue.append((nx,ny))
                    
    return True
                    
    

                    
                      
    

T=int(input())


dx=[-1,1,0,0]
dy=[0,0,-1,1]
cnt=0
for i in range(T):
    cnt=0
    M,N,K=map(int,input().split())
    
    visitied=[[0]*M for _ in range(N)]
    graph=[[0]*M for _ in range(N+1)]
    
    for j in range(K):
        a,b=map(int,input().split())
        
        graph[b][a]=1
        
    for i in range(N):
        for j in range(M):
            if graph[i][j]==1 and visitied[i][j]==0:
                if bfs(i,j)==True:
                    cnt+=1
                
                
    
    print(cnt)
        


    

