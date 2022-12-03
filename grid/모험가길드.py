## 핵심문제: X의 공포도를 가진 유저는 반드시는 X명의 그룹을 이뤄야한다.
N=int(input())

array=list(map(int,input().split()))

group=0
member=0

for i in array:
    member+=1
    
    if i<=member:
        group+=1
        member=0
        
print(group)