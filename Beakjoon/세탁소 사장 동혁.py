changes=[25,10,5,1]

n=int(input())


for i in range(n):
    
    C=int(input())
    result=[]
    
    for j in range(4):
        
        result.append(C//changes[j])
        C=C%changes[j]
        
    
    print(' '.join(map(str,result)))