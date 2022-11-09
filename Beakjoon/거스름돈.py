money=int(input(""))
money=1000-money
list=[500,100,50,10,5,1]
count=0
for i in range(len(list)):
    count=count+money//list[i]
    money=money%list[i]
print(count)