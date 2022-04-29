import sys
from collections import defaultdict
while(True):
    n,m = map(int,sys.stdin.readline().rstrip().split())
    if n==0 and m==0:
        break
    check = defaultdict(int)
    for _ in range(n):
        check[int(sys.stdin.readline().rstrip())]=1
    ans = 0
    for _ in range(m):
        ans += check[int(sys.stdin.readline().rstrip())]
    print(ans)
