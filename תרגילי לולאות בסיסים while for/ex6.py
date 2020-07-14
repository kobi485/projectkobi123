num = int(input('what is the number?'))
cnt = 0
sum = 0
cntt = 0
summ = 0
while 0 <= num <= 100:
    if num >= 60:
        cnt += 1
        sum += num
    if num <= 60:
        cntt += 1
        summ += num
    num = int(input('what is the number?'))
print(sum / cnt)
print(summ / cntt)
