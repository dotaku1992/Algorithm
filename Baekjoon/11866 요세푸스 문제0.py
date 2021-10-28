from collections import deque
n,k = map(int,input().split())
arr =deque(range(1,n+1))
cnt = 1
ans = []

while arr:
    p = arr.popleft()
    if cnt%k==0:
        ans.append(p)
    else:
        arr.append(p)
    cnt+=1
print(f"<{', '.join(map(str,ans))}>")



