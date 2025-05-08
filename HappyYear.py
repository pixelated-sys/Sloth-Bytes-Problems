def nxtHappyYear(year):
    l = len(str(year))
    c=1
    while 1:
        year = year+1
        happyYear = set(str(year))
        if len(happyYear) == l:
            return year

inp = [2017,1990,2021]
for i in inp:
    print(i,"-->",nxtHappyYear(i))