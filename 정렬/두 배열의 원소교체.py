N,K=map(int,input().split())

A=list(map(int,input().split()))
B=list(map(int,input().split()))
A.sort()
B.sort()
count=0
while(1):
    
    A[count]=B.pop()
    
    
    count+=1
    
    if count==K:
        break
    
print(sum(A))
