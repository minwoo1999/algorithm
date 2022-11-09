import re


n=int(input("")) ## 갯수

list=[int(input()) for _ in range(n)] ##무게
list.sort(reverse=True)
lst=[]
for i in range(1,n+1):
    lst.append(i*list[i-1])
    
print(max(lst))