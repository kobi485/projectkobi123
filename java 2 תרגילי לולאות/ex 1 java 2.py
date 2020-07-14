sum = 0
ssum = 0
for i in range(5):
    fac = int(input('enter factor:'))
    num = int(input('enter number:'))
    new = (num + (num * fac / 100))
    ssum += num
    print(new)
    sum += new
print(sum / 5, ssum / 5, sum / 5 - ssum / 5)
