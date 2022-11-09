num=int(input(""))
count=1
stack=[]
result=[]


for i in range(1,num+1):
    
    data=int(input(""))
    
    print("data=",data)
    
    while count<=data:
        
        stack.append(count)
        count+=1
        result.append("+")
    if stack[-1]==data:
        stack.pop()
        result.append("-")
            
    else:
        print("NO")
        exit(0)
            
    print(stack)   
print('\n'.join(result))    
        
    
    
    
    
