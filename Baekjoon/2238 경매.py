from collections import defaultdict
import sys

u, n = sys.stdin.readline().rstrip().split()

arr = defaultdict(tuple)

for _ in range(int(n)):
    name, gold = sys.stdin.readline().rstrip().split()
    gold = int(gold)
    if not arr[gold]:
        arr[gold] = (1, gold, name)
    else:
        arr[gold] = (arr[gold][0] + 1, arr[gold][1], arr[gold][2])
foransarr = sorted(arr.values(), key=lambda x: (x[0], x[1]))
print(foransarr[0][2], foransarr[0][1])
