import sys

n, arr = int(input()), list(map(int, sys.stdin.readline().rstrip().split()))
arr.sort()
print(' '.join(map(str, arr)))
