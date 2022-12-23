import sys
import heapq
input = sys.stdin.readline

n = int(input().strip())
hq = []

for _ in range(n):
    print(hq)
    nums=list(map(int,input().split()))
    
    if not hq:
        for num in nums:
            heapq.heappush(hq,num)
    else:
        
        for num in nums:
            if hq[0]<num:
                heapq.heappush(hq,num)
                heapq.heappop(hq)
                

print(hq[0])
            
        
        
        