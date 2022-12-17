def dfs(x,y):
    
    global cnt
    graph[x][y]='E'
    for i in range(4):
        nx=x+dx[i]
        ny=y+dy[i]
        
        if -1<nx<m and -1<ny<n:
            if graph[nx][ny]=='W':
                graph[nx][ny]=1
                cnt+=1
                dfs(nx,ny)


    return cnt

def dfs2(x,y):
    
    global enemy_cnt
    graph[x][y]='E'
    for i in range(4):
        nx=x+dx[i]
        ny=y+dy[i]
        
        if -1<nx<m and -1<ny<n:
            if graph[nx][ny]=='B':
                graph[nx][ny]='E'
                enemy_cnt+=1
                dfs2(nx,ny)


    return enemy_cnt
            

n,m=map(int,input().split())

# 각 노드가 연결된 정보를 표현
graph = [list(map(str, input())) for _ in range(m)]
    
# 상하좌우
dx=[-1,1,0,0]
dy=[0,0,-1,1]
cnt=1
enemy_cnt=1
our_team=[]
enemy_team=[]
for i in range(m):
    for j in range(n):
        if graph[i][j]=='W':
            dfs(i,j)
            our_team.append(cnt**2)
            cnt=1
            
for i in range(m):
    for j in range(n):
        if graph[i][j]=='B':
            dfs2(i,j)
            enemy_team.append(enemy_cnt**2)
            enemy_cnt=1
            
print(sum(our_team),sum(enemy_team))
            


            
                