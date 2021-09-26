arr = map(int,input().split())
ans = 0
for val in arr:
    ans +=(val*val)
print(ans%10)