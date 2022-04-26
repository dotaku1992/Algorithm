import string

secretword = ' ' + string.ascii_uppercase + string.ascii_lowercase

n = int(input())
idxs = map(int, input().split())
text = input()

textforcheck = ''
for idx in idxs:
    textforcheck += secretword[idx]

if sorted(textforcheck) == sorted(text):
    print('y')
else:
    print('n')
