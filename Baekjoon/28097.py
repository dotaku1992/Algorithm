import sys

n = int(sys.stdin.readline().rstrip())

arr = list(map(int, sys.stdin.readline().rstrip().split()))
totalhour = sum(arr) + 8 * (n - 1)
print(*divmod(totalhour, 24))
