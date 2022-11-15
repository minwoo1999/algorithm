N=int(input())

array=[]

for i in range(N):
    array.append(int(input()))

array.sort()

result=[]

while(1):
    if 3<=len(array):
        result.append(array.pop())
        result.append(array.pop())
        array.pop()
        
    else:
        result.append(array.pop())
    
    if len(array)==0:
        break



print(sum(result))