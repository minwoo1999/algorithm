import sys
sys.setrecursionlimit(10**4)	# recursion limit 제한 설정

def dfs(x,y):

    graph[x][y]='.'

    global cnt

    for i in range(4):
        nx=x+dx[i]
        ny=y+dy[i]
        if -1<nx<N and -1<ny<M:
            if graph[nx][ny]=='#':
                graph[nx][ny]='.'
                cnt+=1
                dfs(nx,ny)

    return cnt



N,M,K=map(int,input().split())

#상하좌우로 이동

dx=[-1,1,0,0]
dy=[0,0,-1,1]

cnt=1
# 0으로 초기화 된 2차원 배열생성
graph=[['.']*M for _ in range(N)]

#해당하는 영역에 쓰레기표시
for i in range(K):
    x,y=map(int,input().split())
    graph[x-1][y-1]='#'

trash=[]

for i in range(N):
    for j in range(M):

        if graph[i][j]=='#':
            dfs(i,j)
            trash.append(cnt)
            cnt=1


print(max(trash))