day=int(input('what is the day?'))
mounth=int(input('what is the mounth?'))
year=int(input('what is the year?'))
if 0<day<32 and 0<mounth<13 and 1949<year<2020:
    print(day,mounth,str(year)[2:4],sep="/")
else:
    if 0>day or 32<day:
        print('day error')
    if 0>mounth or 13<mounth:
        print('mounth error')
    if 1949>year or 2020<year:
        print('year error')
                   