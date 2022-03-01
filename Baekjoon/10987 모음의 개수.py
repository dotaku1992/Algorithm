text = input()
ans = 0
for c in "aeiou":
    ans += text.count(c)
print(ans)
