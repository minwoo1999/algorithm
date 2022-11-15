num=1
count=0
N=int(input())

M=int(input())


N_div=N%100

N=N-N_div


while(1):
    
    
    if N%M==0:
        break
    
    count+=1
    N=N+num



if count<10:
    print('0'+str(count))
else:
    print(count)