num=int(input('enter number:'))
while 99<num<1000:
     print(str(num%10+num//10%10+num//100))
     num = int(input('enter number:'))
print('error')
