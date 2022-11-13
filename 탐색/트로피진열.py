def display(target):

    now=target[0]
    result=1
    for i in range(1,len(target)):
        
        if now<target[i]:
            result+=1
            now=target[i] 
    
    return result



N=int(input())
array=[]
for i in range(N):
    a=int(input())
    array.append(a)

print(display(array))
array.reverse()
print(display(array))