# 통과 풀이
import sys
n = int(sys.stdin.readline())
ans = 0

# 에라토스테네스의 체
def isPrime(n):
    sieve = [True] * (n+1)
    m = int(n ** 0.5)
    for i in range(2, m+1):
        if sieve[i] == True:            
            for j in range(2*i, n+1, i):                 
                sieve[j] = False

    return [i for i in range(2,n+1) if sieve[i] == True]

# 투포인터로 연속합 구하기
tmp = isPrime(n)
left, right = 0, 0  # left, right 사이 거리를 이전 코드보다 가깝게 설정해서 O(right-left) 시간 단축
while right <= len(tmp):
    val = sum(tmp[left:right])
    if val == n:
        ans += 1
        left += 1
    elif val < n:
        right += 1
    else:
        left += 1
print(ans)