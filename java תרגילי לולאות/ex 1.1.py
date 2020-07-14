sum = 0
cnt = 0
max = 0
mid = 0
num = int(input('what is your number?'))
while 0 <= num <= 100:
    if num > max:
        max = num
    sum += num
    cnt += 1
    mid = sum / cnt
    num = int(input('what is your number?'))

print('the highest:', sum / cnt, '\n', 'the max:', max, '\n', 'the fresh:', max - mid)
