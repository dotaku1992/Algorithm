import sys
from collections import defaultdict

n = int(sys.stdin.readline().rstrip())
record = defaultdict(lambda: 1)
ans = 0
for _ in range(n):
    a, b = map(int, sys.stdin.readline().rstrip().split())
    ans += (record[a] != b)
    record[a] = int(not b)
    # 1 in , 0 out
plusans = [1 for ele in record.values() if ele == 0]

print(ans + len(plusans))
