import sys
from collections import defaultdict

n, q = map(int, sys.stdin.readline().rstrip().split())
cnt = defaultdict(int)
text = 'SciComLove'
capscnt = 3 * (n // 10) + len([text[t] for t in range(n % 10) if text[t].isupper()])

for _ in range(q):
    x = int(sys.stdin.readline().rstrip())
    cnt[x] += 1
    if cnt[x] % 2 == 0:
        capscnt = capscnt + (1 if text[(x - 1) % 10].isupper() else -1)
    else:
        capscnt = capscnt + (1 if text[(x - 1) % 10].islower() else -1)
    print(capscnt)
