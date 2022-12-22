# 특정한 자연수의 모든 약수를 찾을 때 약수(제곱근)까지만 확인하면된다.


import math

def is_prime_number(x):
    
    for i in range(2,int(math.sqrt(x))+1):
        
        if x%i==0:
            return False
        
    return True

print(is_prime_number(4))
print(is_prime_number(7))