from itertools import combinations

a=list(map(int,input("").split()))

result=[]
for i in range(1,a[0]+1):
    result.append(i)

per=list(combinations(result,a[1]))

for i in per:
    print(' '.join(map(str,i)))