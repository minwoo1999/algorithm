count=1
list=[]
list2=[]
for row in range(10):
    num=int(input(""))
    num=num%42
    list.append(num)

list.sort()
for i in list:
    if i not in list2:
        list2.append(i)

for i in range(len(list2)):
    if(list2[0]!=list2[i]):
        count+=1
print(count)