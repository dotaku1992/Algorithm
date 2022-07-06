import sys

n = int(sys.stdin.readline().rstrip())
monthToMaxDay = [0, 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
for _ in range(n):
    a, b = map(int, sys.stdin.readline().rstrip().split())
    firstboolean = all([0 <= a <= 23, 0 <= b <= 59])
    secondboolean = all([1 <= a <= 12, a <= 12 and 1 <= b <= monthToMaxDay[a]])
    print(f"{'Yes' if firstboolean else 'No'} {'Yes' if secondboolean else 'No'}")
