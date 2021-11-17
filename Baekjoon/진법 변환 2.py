from string import ascii_uppercase
n,b = map(int,input().split())
arr = "0123456789"+ascii_uppercase
ans = []
while n:
    idx = n%b
    ans.append(arr[idx])
    n = n//b
print(''.join(ans[::-1]))
