import sys

lotation, n = sys.stdin.readline().rstrip().split()
n = int(n)
arr = []
for _ in range(n):
    arr.append(list(map(int, sys.stdin.readline().rstrip().split())))

yrange = [i for i in range(n)]
xrange = [i for i in range(n)]

if lotation == 'L' or lotation == 'R':
    xrange = xrange[::-1]
else:
    yrange = yrange[::-1]

convertDict = {2: 5, 5: 2, 1: 1, 8: 8}
for yidx in yrange:
    for xidx in xrange:
        print(convertDict.get(arr[yidx][xidx], '?'), end=' ')
    print()
