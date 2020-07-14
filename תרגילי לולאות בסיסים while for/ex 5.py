num=int(input('what is the number?'))
cnt=0
sum=0
while 0<=num<=100:
    if num>=60:
        cnt+=1
        sum+=num
    num=int(input('what is the number?'))
print(sum/cnt)



    