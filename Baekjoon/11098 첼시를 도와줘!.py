import sys
T =int(input())

for _ in range(T):
    n = int(input())
    ans = None
    for _ in range(n):
        price , name = sys.stdin.readline().rstrip().split()
        if ans ==None or ans[0] < int(price):
            ans = (int(price),name)
    print(ans[1])