convertable = {'-': 0, '\\': 1, '(': 2,
               '@': 3, '?': 4, '>': 5, '&': 6, '%': 7, '/': -1}
while True:
    text = input()
    if text == '#':
        break
    ans = 0
    power = len(text) - 1
    for ele in text:
        ans += convertable[ele] * (8 ** power)
        power -= 1
    print(ans)
