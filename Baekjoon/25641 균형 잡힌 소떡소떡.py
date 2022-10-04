n = int(input())
text = input()
cnt = {'t': 0, 's': 0}
length = 0
for e in text[::-1]:
    cnt[e] += 1
    if (cnt['t'] == cnt['s']):
        length = cnt['t']
print(text[-length * 2:])
