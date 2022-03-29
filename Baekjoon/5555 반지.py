text = input()
n = int(input())
ans = 0
for _ in range(n):
    sub_text = input() * 2
    ans += (sub_text.find(text) != -1)
print(ans)