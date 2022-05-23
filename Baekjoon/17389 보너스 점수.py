n = int(input())
text = input()
ans = 0
bonus = 0
for defaultscore, val in enumerate(text, 1):
    if val == 'O':
        ans += bonus + defaultscore
        bonus += 1
    else:
        bonus = 0

print(ans)
