import sys
from collections import defaultdict

# STRAWBERRY, BANANA, LIME, PLUM  : max 5개

n = int(sys.stdin.readline().rstrip())
check = defaultdict(int)
for _ in range(n):
    fruitname, cnt = sys.stdin.readline().rstrip().split()
    check[fruitname] += int(cnt)
print("YES" if any(filter(lambda x: x == 5, check.values())) else "NO")
