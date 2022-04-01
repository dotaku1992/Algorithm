n = int(input())
arr = [int(input()) for _ in range(n)]
arr.sort()
ans = 5
for idx,val in enumerate(arr):
    cnt = 0
    for val2 in arr[idx:idx+5]:
        if val<=val2 <=val+4:
            cnt+=1
    ans = min(ans,5-cnt)
print(ans)