import sys

n = int(sys.stdin.readline().rstrip())
cnt, cat = 0, 0

while cat < n:
    if cat == 0:
        cat = 1
    else:
        cat *= 2
    cnt += 1
print(cnt)
