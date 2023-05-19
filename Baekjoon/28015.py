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
    cnt1, cnt2 = 0, 0
    for ele in checkarr:
        if ele == 0:
            ans += (min(cnt1, cnt2) + (1 if max(cnt1, cnt2) > 0 else 0))
            cnt1, cnt2 = 0, 0
        else:
            cnt1, cnt2 = cnt1 + (ele == 1), cnt2 + (ele == 2)
    ans += (min(cnt1, cnt2) + (1 if max(cnt1, cnt2) > 0 else 0))

print(ans)
