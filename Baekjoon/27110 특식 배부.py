import sys

n = int(sys.stdin.readline().rstrip())
a, b, c = map(int, sys.stdin.readline().rstrip().split())
print(min(a, n) + min(b, n) + min(c, n))
