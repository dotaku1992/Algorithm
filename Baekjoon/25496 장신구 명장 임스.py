tiredgage, N = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()
ans = 0
lefttiredgage = 200 - tiredgage
idx = 0
while (lefttiredgage > 0 and idx < len(arr)):
    lefttiredgage -= arr[idx]
    idx += 1
    ans += 1
print(ans)
