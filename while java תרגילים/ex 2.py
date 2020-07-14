age=int(input('what is your age?'))
while 0<=age<121:
    if 0 <= age < 18:
        print('child')
    elif age <= 60:
        print('adult')
    elif age <= 120:
        print('senior')
    age = int(input('what is your age?'))
print("end")



