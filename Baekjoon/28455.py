import sys


def getstatFromlv(lv: int):
    union = [60, 100, 140, 200, 250]
    stat = 0
    for ele in union:
        if ele <= lv:
            stat += 1
        else:
            break
    return stat


n = int(sys.stdin.readline().rstrip())
totallv, stat = 0, 0
arr = []
for _ in range(n):
    lv = int(sys.stdin.readline().rstrip())
    arr.append(lv)

arr.sort(reverse=True)

for idx in range(min(42, n)):
    totallv += arr[idx]
    stat += getstatFromlv(arr[idx])

print(totallv, stat)
