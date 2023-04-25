import sys

n,m = map(int,sys.stdin.readline().rstrip().split())
print("Yes" if n*100 >= m else "No")