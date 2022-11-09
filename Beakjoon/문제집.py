import sys

num=int(sys.stdin.readline())

cnt=0
while(num>0):
    
    if num%5==0:
        cnt=cnt+num//5
        break
    else:
        cnt+=1
        num-=2
        if num<0:
            cnt=-1

print(cnt)
    
    
    
    
    
    

    
    
    
    