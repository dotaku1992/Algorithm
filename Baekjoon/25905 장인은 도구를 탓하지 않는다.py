import sys
arr = []
for _ in range(10):
    arr.append(float(sys.stdin.readline().rstrip()))
arr.sort()
ans = 1
for div,ele in enumerate(arr[1:],1):
    ans= ans*ele/div
print('{:.6f}'.format(ans*10**9))
