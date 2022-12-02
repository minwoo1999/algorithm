n=int(input())

array=[]
for i in range(n):
    
    name,point=input().split()
    array.append((name,int(point)))
    
array=sorted(array,key=lambda x:x[1])

for i in array:
    print(i[0],end=" ")