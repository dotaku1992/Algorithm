l = int(input())
text = input()
r = 31
M = 1234567891
hashval = 0
for idx, val in enumerate(text):
    hashval += (ord(val) - ord('a') + 1) * r ** idx
print(hashval % M)
