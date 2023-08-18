import sys
from datetime import date

currentdate = date(*map(int, sys.stdin.readline().rstrip().split('-')))
cnt = 0
for _ in range(int(sys.stdin.readline().rstrip())):
    nxtdate = date(*map(int, sys.stdin.readline().rstrip().split('-')))
    if nxtdate >= currentdate:
        cnt += 1
print(cnt)
