T = int(input())

def monthToday(day: int, y: int):
    mTodays = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    mTodays[2] += (y % 100 != 0 and y % 4 == 0) or y % 400 == 0
    for month, ele in enumerate(mTodays):
        if day > ele:
            day -= ele
        else:
            return month, day


for _ in range(T):
    mTodays = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    y, md = map(int, input().split())
    iscuryearyun = (y % 100 != 0 and y % 4 == 0) or y % 400 == 0
    mTodays[2] += iscuryearyun
    curday = sum(mTodays[:md])
    if curday <= 0:
        y -= 1
        curday = 365 + ((y % 100 != 0 and y % 4 == 0) or y % 400 == 0) - curday
    ansm, ansd = monthToday(curday, y)
    print(f"{y} {ansm} {ansd}")
