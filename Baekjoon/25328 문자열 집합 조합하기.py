from itertools import combinations
from collections import defaultdict

texts = [input() for _ in range(3)]
k = int(input())
cnt = defaultdict(int)

for text in texts:
    for c in combinations(text, k):
        cnt[''.join(c)] += 1

anslist = [k for k, v in cnt.items() if v >= 2]
anslist.sort()

if anslist:
    print(*anslist, sep='\n')
else:
    print(-1)
