num=int(input('what is the number?'))
if 1000>num>99:
    print((num%10)+(num//10%10)+(num//100))
else:
    print('error')