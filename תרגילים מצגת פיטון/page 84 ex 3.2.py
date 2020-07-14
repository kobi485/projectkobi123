num1=int(input('enter number 1:'))
num2=int(input('enter number 2:'))
num3=int(input('enter number 3:'))
if num1>num2:
    max=num1
else:
    max=num2
if num3>max:
    max=num3
print(max)