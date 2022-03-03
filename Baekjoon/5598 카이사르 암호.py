import string
arr = string.ascii_uppercase
arr2 = arr[3:] + arr[0:3]

text = input()
ans = ""
for c in text:
    ans +=arr[arr2.index(c)]
print(ans)


