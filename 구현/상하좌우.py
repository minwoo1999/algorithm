N=int(input())

plan=input().split()
x,y=1,1
dx=[0,0,-1,1]
dy=[-1,1,-0,0]

route=['L','R','U','D']


for i in plan:
    for j in range(len(route)):
        
        if i ==route[j]:
            nx=x+dx[j]
            ny=y+dy[j]
            
    if nx<1 or ny<1 or nx>N or ny>N:
        continue
    
    x,y=nx,ny
print(x,y)     


