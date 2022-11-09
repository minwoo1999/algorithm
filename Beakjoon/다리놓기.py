import math

num=int(input(""))

for i in range(num):
    a=list(map(int,input("").split()))
    result=math.factorial(a[1])//(math.factorial(a[1]-a[0])*math.factorial(a[0]))
    print(result)
    
    