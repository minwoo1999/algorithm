N=int(input())

route=input().split()
x,y=1,1
#상하ㅘ우
dx=[-1,1,0,0]
dy=[0,0,-1,1]
move_type=['U','D','L','R']

for i in route:

    for j in range(4):
        if i==move_type[j]:
            nx=x+dx[j]
            ny=y+dy[j]

    if nx<1 or N<nx or ny<1 or N<ny:
        continue
    
    else:
        x=nx
        y=ny

print(x,y)
        