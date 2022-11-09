num=input()



num=num.replace('XXXX','AAAA')
num=num.replace('XX','BB')


if 'X' in num:
    print("-1")
else:
    print(num)