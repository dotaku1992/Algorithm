import sys

n = int(sys.stdin.readline().rstrip())
text = sys.stdin.readline().rstrip()
ans = 0

for i in range(n // 2):
    ans += (text[i] != text[-(i + 1)])
print(ans)
