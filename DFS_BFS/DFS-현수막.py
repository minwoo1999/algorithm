import sys
sys.setrecursionlimit(10 ** 6)
def dfs(x,y):

    if x <= -1 or x >= N or y <= -1 or y >= M:
        return False

    if graph[x][y]==1:
        graph[x][y]=0
        dfs(x-1,y) 
        dfs(x+1,y) 
        dfs(x,y-1) 
        dfs(x,y+1) 
        dfs(x-1,y-1) 
        dfs(x-1,y+1) 
        dfs(x+1,y+1)  
        dfs(x+1,y-1)

        return True
    return False


N,M=map(int,sys.stdin.readline().split())

graph=[]
for i in range(N):
    graph.append(list(map(int,sys.stdin.readline().split())))


result=0

for i in range(N):
    for j in range(M):
        if graph[i][j]==1:
            dfs(i,j)
            
            result+=1

print(result)