import sys

n, x = map(int, sys.stdin.readline().rstrip().split())
arr = list(map(int, sys.stdin.readline().rstrip().split()))
startidx = 0
while True:
    if arr[startidx % n] < x + 1 * startidx:
        print(startidx % n + 1)
        break
    else:
        startidx += 1
