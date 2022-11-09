n = int(input())

def sum_num(input):
    result=0
    for i in input:
        if i.isdigit():
            result+=int(i)
    
    print(result)
    return result




arr = []
for i in range(n):
    a = input()
    arr.append(a)
    
    
arr.sort(key=lambda x:(len(x),sum_num(x),x))

for i in arr:
    print(i)
