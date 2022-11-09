avg=0
sum=0
count=0
num=int(input(""))
result=[]


for i in range(num):
    student=list(map(int,input("").split()))
    for j in range(len(student)):
        studentsum=student[0]
        if(j!=0):
            sum+=student[j]
            
    avg=sum/studentsum
    for j in range(len(student)):
       
        if(j!=0 and avg<student[j]):
            count+=1
    portion=count/student[0]*100
    result.append(portion)
    portion=0
    avg=0
    sum=0
    count=0

for i in range(len(result)):
    print("%.3f" % result[i],"%")