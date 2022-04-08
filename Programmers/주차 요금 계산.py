from collections import defaultdict
import math
def timetomin(text:str):
    h,m = text.split(':')
    output = int(h)*60 + int(m)
    return output

def solution(fees, records):
    bt,bp,divt,divp = fees
    print(bt,bp,divt,divp)

    cartable = defaultdict(list)
    for texts in records:
        timestr,carno,status = texts.split()
        cartable[carno].append(timestr)

    for no in cartable:
        if len(cartable[no])%2==1:
            cartable[no].append("23:59")

    sortedcarno = sorted(cartable.keys())
    answer = []

    for carkeyno in sortedcarno:
        allminute = 0
        for idx in range(len(cartable[carkeyno])//2):
            allminute += timetomin(cartable[carkeyno][2*idx+1])-timetomin(cartable[carkeyno][2*idx])
        if allminute <= bt:
            answer.append(bp)
        else:
            answer.append(bp + math.ceil((allminute-bt)/divt)*divp)

    return answer

