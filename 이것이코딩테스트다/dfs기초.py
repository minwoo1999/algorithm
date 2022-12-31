def dfs(graph,v,visited):
    
    visitied[v]=True
    print(v,end=" ")
    
    for i in graph[v]:
        if visitied[i]==False:
            dfs(graph,i,visited)


graph=[[],[2,3,8],[1,7],[1,4,5],[3,5],[3,4],[7],[2,6,8],[1,7]]


visitied=[False]*len(graph)



dfs(graph,1,visitied)