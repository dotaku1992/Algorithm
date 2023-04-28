import sys
from collections import defaultdict

n = int(sys.stdin.readline().rstrip())
texts = sys.stdin.readline().rstrip()
cnt = defaultdict(int)
for c in texts:
    cnt[c] = 1

print("YES" if len(cnt.keys()) >= 2 else "NO")
