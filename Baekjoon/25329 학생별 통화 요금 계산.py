import math
import sys
from collections import defaultdict

n = int(input())
timesrecorddict = defaultdict(int)
for _ in range(n):
    hm, name = sys.stdin.readline().rstrip().split()
    h, m = hm.split(':')
    summin = int(h) * 60 + int(m)
    timesrecorddict[name] += summin

arr = []
for name in timesrecorddict:
    price = 10 + 3 * (timesrecorddict[name] > 100) * (math.ceil((timesrecorddict[name] - 100) / 50))

    arr.append((price, name))
arr.sort(key=lambda x: (-x[0], x[1]))
for p, name in arr:
    print(name, p)
