N,M=map(int,input().split())

result=[]
for i in range(N):
    array=list(map(int,input().split()))
    
    result.append(min(array))
    
print(max(result))
    
    