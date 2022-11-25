from bisect import bisect_right,bisect_left


def bisect(array,right,left):
    
    right_biset=bisect_right(array,right)
    left_biset=bisect_left(array,left)
    
    return right_biset-left_biset




N,X=map(int,input().split())


array=list(map(int,input().split()))

array.sort()

result=bisect(array,X,X)

## 선형탐색

##for i in array:
##    if i==X:
##        result+=1
        
if result==0:
    print("-1")
else:
    print(result)
