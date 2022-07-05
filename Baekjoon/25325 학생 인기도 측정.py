from collections import defaultdict

n = int(input())
cnt = defaultdict(int)
for name in input().split():
    cnt[name] = 0

for _ in range(n):
    names = list(input().split())
    for name in names:
        cnt[name] += 1

anslist = [(name, c) for name, c in cnt.items()]
anslist.sort(key=lambda x: (-x[1], x[0]))
for name, c in anslist:
    print(name, c)
