cnt = 0
pas = int(input('enter password?'))
ppas = int(input('enter password:'))
while pas != ppas:
    cnt += 1
    if cnt == 5:
        print('faild')
        break
    print('error')
    ppas = int(input('enter password:'))
else:
    print('succses')
