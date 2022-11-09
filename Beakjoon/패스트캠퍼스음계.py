janjo=list(map(int,input().split()))

result=sorted(janjo)
reverse_result=sorted(janjo,reverse=True)
count=0
reverse_count=0
for i in range(len(janjo)):
    
    if result[i]==janjo[i]:
        count+=1
    if reverse_result[i]==janjo[i]:
        reverse_count+=1
    if i==7:
        if count==8:
            print("ascending")
        elif reverse_count==8:
            print("descending")
        else:
            print("mixed")