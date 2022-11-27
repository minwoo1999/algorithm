def dfs(i,j):
    
    
    if i<0 or i>=N or j<0 or j>=M:
        return False
    
    if graph[i][j]==0:
        graph[i][j]=1
        
        ## 상하좌우
        dfs(i-1,j)
        dfs(i+1,j)
        dfs(i,j-1)
        dfs(i,j+1)
        print(dfs(i-1,j))
        print(dfs(i+1,j))
        print(dfs(i,j-1))
        print(dfs(i,j+1))
        ### 얼음판 안에있으며 얼음판에 해당하는값이
        ### 0일경우 1로 바꿔주고 상하좌우에 있을때까지 1로 전부 변환
        ### return True 로 count하나씩 늘림
        
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
    
    
    
    
    
