## 바텀업 메모제이션

d=[0]*100

d[1]=1
d[2]=1

n=4

for i in range(3,n+1):
    
    d[i]=d[i-1]+d[i-2]
    
    
print(d[n])