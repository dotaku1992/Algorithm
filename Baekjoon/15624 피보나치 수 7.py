import sys
div = 1000000007
n = int(sys.stdin.readline().rstrip())
f,s = 0,1
if n ==0:
    print(0)
elif n == 1:
    print(1)
else:
    for _ in range(n-1):
        f,s = s%div,(f+s)%div
    print(s)

