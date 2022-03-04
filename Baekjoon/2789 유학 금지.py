text = input()
ans = ""
for c in text:
    if c in "CAMBRIDGE":
        continue
    ans+=c
print(ans)