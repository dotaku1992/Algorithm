import sys

n, m = map(int, sys.stdin.readline().rstrip().split())

ans = 0
for _ in range(n):
    arr = list(map(int, sys.stdin.readline().rstrip().split()))
    checkarr = []
    cnt = [0, 0, 0]
    for ele in arr:
        if checkarr and checkarr[-1] == ele:
            pass
        else:
            checkarr.append(ele)
            cnt[ele] += 1
    ans = ans + cnt[1] + cnt[2]
    
print(ans)
