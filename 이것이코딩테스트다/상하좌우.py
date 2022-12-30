N=int(input())

plans=list(input())

#상하좌우 이동
x,y=1,1
dx=[-1,1,0,0]
dy=[0,0,-1,1]
route=['U','D','L','R']
for i in plans:
    for j in range(4):
        if i==route[j]:
            
            nx=x+dx[j]
            ny=y+dy[j]
            print(nx,ny)
            if nx<1 or N<ny or ny<1 or N<ny:
                continue
            else:
                x=nx
                y=ny

                
    
    
print(x,y)
    
        
            
        
    
    
    
    
            
    
    
    