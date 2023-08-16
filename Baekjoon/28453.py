import sys

n = int(sys.stdin.readline().rstrip())
inputs = list(map(int, sys.stdin.readline().rstrip().split()))

lv = [4] * 250 + [3] * (275 - 250) + [2] * (300 - 275) + [1]
print(*[lv[inputs[idx]] for idx in range(n)])
