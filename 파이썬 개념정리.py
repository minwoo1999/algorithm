## 2차원 배열을 쉽게 초기화하는방법
'''
n=3
m=4

array=[[0]*m for _ in range(n)]

print(array)

## 잘못된 예 [1][1]만 5로 바꾸었을 뿐인데 3개의 리스트에서 인덱스 1에
##해당한느 원소가 전부다 1로 바뀐것을 알수있다.
## 반드시 리스트 컴프리 헨션을 이용해야한다.

n=3
m=4

array=[[0]*m]*n
print(array)

array[1][1]=5
print(array)
'''
## heapq 라이브러리 다익스트라 최단경로 알고리즘을 포함해
## 다양한 알고리즘에서 우선순위 큐 기능을 구현하고자 할때 사용된다.

## queue라이브러리를 사용할수있지만 코테환경에선 heapq가 더 빠르다
## heapq는 전부 넣었다가 빼는것만으로 시간복잡도 O에 오름차순 정렬 완료
## heapq.heappush() 로 삽입
## heapq.heappop() 메서드로 꺼낼수있음

import heapq

def heapsort(num):
    result=[]
    h=[]
        
    for value in num:
        heapq.heappush(h,value)
        
    for _ in range(len(h)):
        result.append(heapq.heappop(h)) ##가장 작은원소부터 제거
    return result
    
result=heapsort([1,3,5,7,9,2,4,6,8,0])

print(result)
        