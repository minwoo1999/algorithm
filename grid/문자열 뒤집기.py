arr=input()

count0=0
count1=0
if arr[0]=="1":
    count0+=1
else:
    count1+=1
    


for i in range(2,len(arr)-1):
    if arr[i]!=arr[i+1]:
        
        if arr[i+1]=="1":
            count0+=1
        else:
            count1+=1
            

print(min(count0,count1))