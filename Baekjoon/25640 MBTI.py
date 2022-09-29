import sys
mymbti = sys.stdin.readline().rstrip()
ans = 0
for _ in range(int(sys.stdin.readline().rstrip())):
    yourmbti = sys.stdin.readline().rstrip()
    ans += (yourmbti == mymbti)
print(ans)