import sys

n = int(sys.stdin.readline().rstrip())
arr = list(map(int, sys.stdin.readline().rstrip().split()))
cur_v = 0

for ai in arr:
    print(f'{100 - (100 - cur_v) * (1 - ai / 100):.6f}')
    cur_v = 100 - (100 - cur_v) * (1 - ai / 100)
