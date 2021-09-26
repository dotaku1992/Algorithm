import sys

for _ in range(3):
    n = int(sys.stdin.readline().rstrip())
    sum_v = 0
    for _ in range(n):
        sum_v += int(sys.stdin.readline().rstrip())
    if sum_v == 0:
        print(0)
    elif sum_v >0:
        print('+')
    else:
        print('-')