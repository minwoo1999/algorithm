num=int(input(""))
count=0
previous=""
result=0
for i in range(num):
    quiz=list(input(""))

    for i in range(len(quiz)):
        if(quiz[i]=='O'):
            count+=1 ## O일 경우 1을 증가시킴
            if(quiz[i]==previous):
                result+=count
            else:
                result+=1
            previous=quiz[i]
        else:
            previous=quiz[i]
            count=0
        
    print(result)
    count=0
    previous=""
    result=0
          
                

