def binary_search(array,target,start,end):

    while(start<=end):

        mid=(start+end)//2

        if array[mid]==target:
            return mid
        elif target<array[mid]:
            end=mid-1
        else:
            start=mid+1
    
    return False
N=int(input())
array=list(map(int,input().split()))

array.sort()

M=int(input())
x=list(map(int,input().split()))

for i in x:

    result=binary_search(array,i,0,N-1)

    if result!=False:
        print('yes',end=' ')
    else:
        print('no',end=' ')
