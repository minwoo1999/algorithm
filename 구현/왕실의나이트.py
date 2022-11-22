l=list(input())
cnt=0

a=ord(l[0])-96 ## 아스키코드로 값으로 변환한다.
b=int(l[1])

dx = [-1,1,2,2,1,-1,-2,-2]
dy = [2,2,1,-1,-2,-2,-1,1]   ##갈수있는 경우의 수 8가지

for i in range(len(dx)): ##갈수있는 경우의 수 만큼 len \

    nx=a+dx[i] ## 현재위치에서 경우의수 만큼 더해서 좌표를 바꿈
    ny=b+dy[i]

    if nx<=8 and ny<=8 and 1<=nx and 1<=ny: ## 범위안에있으면 카운트
        cnt+=1

print(cnt)