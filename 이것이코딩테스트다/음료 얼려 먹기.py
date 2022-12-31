

def dfs(i,j):
    
    if i<0 or N<=i or j<0 or M<=j:
        return False
    
    if graph[i][j]==0:
        
        graph[i][j]=1
        
        for k in range(4):
            nx=i+dx[k]
            ny=j+dy[k]
            
            dfs(nx,ny)
        
        return True
    
    return False
    


N,M=map(int,input().split())

graph=[]

for i in range(N):
    graph.append(list(map(int,input())))
    

dx=[-1,1,0,0]
dy=[0,0,-1,1]

result=0
for i in range(N):
    for j in range(M):
        if dfs(i,j):
            result+=1
            
print(result)