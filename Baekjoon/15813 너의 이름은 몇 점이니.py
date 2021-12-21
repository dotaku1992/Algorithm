import string
table ={}
for al,num in zip(string.ascii_uppercase,range(1,27)):
    table[al] = num

n = int(input())
text = input()

ans = 0
for ele in text:
    ans +=table[ele]

print(ans)