'''
def binary_serach(array,target,start,end):
    
    count=0
    while(start<=end):
        mid=(start+end)//2
        if array[mid]==target:
            count+=1
        elif array[mid]<target:
            start=mid+1
        else:
            end=mid-1
        
        if 1<count:
            return "yes"
    
    return "no"

    

N=int(input())
A=list(map(int,input().split()))

A.sort()


B=list(set(A))

count=0
for i in B:
    result=binary_serach(A,i,0,len(A))
    if result=="yes":
        count+=1
        
        
print(count)
'''

import sys
from bisect import bisect_left
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))
stack = [-sys.maxsize]

for i in A:
    if stack[-1]<i:
        stack.append(i)
    else:
        stack[bisect_left(stack,i)]=i

print(len(stack)-1)