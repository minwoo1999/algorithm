import sys

n=int(sys.stdin.readline())
count=0


while(0<n):
    if n%5==0:
        n-=5
        count+=1
    else:
        n-=3
        count+=1
            

if n<0:
    print(-1)
else:

    print(count)