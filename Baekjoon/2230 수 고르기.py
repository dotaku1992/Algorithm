import sys
n,m = map(int,sys.stdin.readline().rstrip().split())
arr = []
for _ in range(n):
    arr.append(int(sys.stdin.readline().rstrip()))
arr.sort()
start,end=0,0
ans = arr[-1]-arr[0]
while start <= end:
    if arr[end]-arr[start] < m:
        if end+1 <n:
            end+=1
        else:
            start+=1

    elif arr[end]-arr[start] > m:
        ans = min(arr[end]-arr[start],ans)
        start+=1
    else:
        ans = m
        break
print(ans)
