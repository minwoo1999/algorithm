a,b=map(int,input().split())


graph=[[] for _ in range(a+1)]

for i in range(a):
    array=list(map(input().split()))
    graph[i].append(array)
    
print(graph)