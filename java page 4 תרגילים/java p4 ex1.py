lnum = 0
num = int(input('enter number?'))
while num != 0:
    if num > 0 and (num < lnum or lnum == 0):
        lnum = num
    num = int(input('enter number?'))
print(lnum)
