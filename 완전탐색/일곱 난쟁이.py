from itertools import combinations
member=[]

for i in range(9):
    N=int(input())
    member.append(N)
    


member=list(combinations(member,7))

member.sort()

for i in member:
    if sum(i)==100:
        for j in sorted(i):
            print(j)
        
        break
        
        



