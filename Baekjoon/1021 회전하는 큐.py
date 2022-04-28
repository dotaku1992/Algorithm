from collections import defaultdict
n = int(input())
check = defaultdict(int)
ans = 0
for no in range(n):
    text = input()
    l = len(text)
    text*=2
    flag = True
    for start in range(0,l+1):
        if check[text[start:start+l]]==0:
            check[text[start:start + l]]=no+1
        elif check[text[start:start+l]]==no+1:
            continue
        else:
            flag=False
    ans +=flag
print(ans)
