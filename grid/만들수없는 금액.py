# coin 정렬 후 코인누적합보다 coin이 크면
#만들수없는 금액의 최소값이 된다.
N=int(input())

coin=list(map(int,input().split()))

coin.sort()
target=1
for i in coin:


    if target<i:
        break
    target+=i

print(target)
