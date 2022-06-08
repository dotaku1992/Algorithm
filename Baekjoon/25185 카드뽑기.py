import sys
from collections import defaultdict


def limit1(arr: list):
    flag = False
    numlist = [int(ele[0]) for ele in arr]
    chrlist = [ele[1] for ele in arr]
    for i in range(0b1111 + 1):
        if bin(i).count('1') == 3:
            idxlist = [m for m in range(4) if (i & (1 << m))]
            check1forchr = defaultdict(int)
            for idx in idxlist:
                check1forchr[chrlist[idx]] += 1
            if len(check1forchr.keys()) == 1:
                sortednumarr = [numlist[idx] for idx in idxlist]
                sortednumarr.sort()
                if sortednumarr[0] + 1 == sortednumarr[1] and sortednumarr[1] + 1 == sortednumarr[2]:
                    flag = True

    return flag


def limit2(arr: list):
    check2 = defaultdict(int)
    for ele in arr:
        check2[ele] += 1

    return any([cnt >= 3 for cnt in check2.values()])


def limit3(arr: list):
    return arr[0] == arr[1] and arr[2] == arr[3]


T = int(sys.stdin.readline().rstrip())

for _ in range(T):
    arr = sys.stdin.readline().rstrip().split()
    arr.sort()
    if any([limit1(arr), limit2(arr), limit3(arr)]):
        print(':)')
    else:
        print(':(')
