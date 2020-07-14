cnt = 0
num = int(input('what is the number?'))
while num != 0:
    if num % 3 == 0 or num % 7 == 0:
        cnt += 1
    num = int(input('what is the number?'))

print(cnt, 'numbers split in 3 and 7')
