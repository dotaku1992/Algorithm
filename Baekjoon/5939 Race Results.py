import sys

n = int(sys.stdin.readline().rstrip())
arr = []
for _ in range(n):
    h, m, s = map(int, sys.stdin.readline().rstrip().split())
    arr.append(h * 60 * 60 + m * 60 + s)
arr.sort()
for sec in arr:
    h, m, s = sec // (60 * 60), (sec % (60 * 60)) // 60, (sec % (60 * 60)) % 60
    print(h, m, s)
