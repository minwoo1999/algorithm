N=input()

mid=(len(N)//2)-1
leftsum=0
rightsum=0
for i in range(len(N)):

    if i<=mid:
        leftsum+=int(N[i])
    else:
        rightsum+=int(N[i])


if leftsum==rightsum:
    print("LUCKY")
else:
    print("READY")