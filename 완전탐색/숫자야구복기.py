from itertools import permutations

N=int(input())

a=['1','2','3','4','5','6','7','8','9']

num=list(permutations(a,3))

for _ in range(N):
    test,s,b=map(int,input().split())
    remove_cnt=0
    test=list(str(test))
    for i in range(len(num)):
        strike=0
        ball=0
        i-=remove_cnt
        for j in range(3):
            
            if num[i][j]==test[j]:
                strike+=1
            elif test[j] in num[i]:
                ball+=1
                
        
        if s!=strike or ball!=b:
            num.remove(num[i])
            remove_cnt+=1
        


print(len(num))