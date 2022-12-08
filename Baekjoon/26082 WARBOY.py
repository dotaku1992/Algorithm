import sys

a, b, c = map(int, sys.stdin.readline().rstrip().split())
print(3 * b * c // a)
