def dfs(x,y):
    
    if x<0 or N<=x or y<0 or M<=y:
        return False
    
    
    if graph[x][y]==0:
        graph[x][y]=1
        
        ##상하좌우
        dfs(x-1,y)
        dfs(x+1,y)
        dfs(x,y-1)
        dfs(x,y+1)
        
        return True
    
    return False



N,M=map(int,input().split())

graph=[]
for i in range(N):
    graph.append(list(map(int,input())))
    
    

result=0

for i in range(N):
    for j in range(M):
        if dfs(i,j):
            result+=1
            
            
print(result)