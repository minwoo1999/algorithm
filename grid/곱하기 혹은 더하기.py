N=input()
result=0
cal=''
array=[]
for i in N:
    array.append(int(i))
    
result=array[0]
for i in range(len(array)-1):
    
    if result<=1 or result<= -1:
        result+=array[i+1]
    else:
        result*=array[i+1]
    

print(result)