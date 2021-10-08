text = list(input())

for idx in range(len(text)):
    if ('a'<=text[idx]<='z') or ('A'<=text[idx] <='Z'):
        stdc = 'A' if text[idx] <='Z' else 'a'
        text[idx] = chr(ord(stdc) + ((ord(text[idx])-ord(stdc))+13)%(ord('z')-ord('a')+1))
print(''.join(text))
