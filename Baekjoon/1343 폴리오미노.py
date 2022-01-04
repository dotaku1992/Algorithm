text = list(input())

for idx, _ in enumerate(text):
    if text[idx:idx + 4] == list('XXXX'):
        text[idx:idx + 4] = list('AAAA')
for idx, _ in enumerate(text):
    if text[idx:idx + 2] == list('XX'):
        text[idx:idx + 2] = list('BB')
if text.count('X') == 0:
    print(''.join(text))
else:
    print(-1)
