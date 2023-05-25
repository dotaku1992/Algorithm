import sys

n, a, b = map(int, sys.stdin.readline().rstrip().split())

if a == b:
    print("Anything")
elif a < b:
    print('Bus')
else:
    print('Subway')
