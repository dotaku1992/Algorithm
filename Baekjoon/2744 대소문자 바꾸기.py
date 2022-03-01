text = input()
ans = ""
for c in text:
    if 'a' <= c <= 'z':
        ans += c.upper()
    else:
        ans += c.lower()
print(ans)
