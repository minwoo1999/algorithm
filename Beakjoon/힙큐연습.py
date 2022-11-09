import heapq

num = [5, 3, 4, 2, 1]
heap = []

for n in num:
    heapq.heappush(heap, (-n, n))  # (우선순위, 값)

print(heap[0])
# 우선순위와 함께 출력
while heap:
    print(heapq.heappop(heap))

"""
(-5, 5)
(-4, 4)
(-3, 3)
(-2, 2)
(-1, 1)
"""