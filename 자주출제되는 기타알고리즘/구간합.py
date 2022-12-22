# 구간합 빠르게 구하기
# N개의 수위치 각각에 대하여 접두사 합을 계산하여 P에 저장한다.
# 매 M개의 쿼리정보를 입력할 때 구간합은 p[right]-p[left-1] 

n=5
data=[10,20,30,40,50]
sum=0
data_sum=[]
data_sum.append(0)
for i in data:
    sum+=i
    data_sum.append(sum)
    
left=3
right=4

print(data_sum[right]-data[left-1])