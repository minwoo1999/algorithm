N,M=map(int,input().split())

array=[]
result=[]
for i in range(N):
    
    array.append(list(map(int,input().split())))
    
for i in array:
    result.append(min(i))
    


print(max(result))