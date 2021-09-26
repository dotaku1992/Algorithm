n = int(input())
cnt = 0
for idx in range(1,n+1):
    strconvert = str(idx)
    cnt+=(strconvert.count('3') + strconvert.count('9') + strconvert.count('6'))
print(cnt)
