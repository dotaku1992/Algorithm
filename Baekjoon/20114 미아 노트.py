n,h,w = map(int,input().split())
texts = [input() for _ in range(h)]
ans = ["?" for _ in range(n)]

for text in texts:
    for idx,val in enumerate(text):
        if val == "?":
            continue
        ans[idx//w]=val
print(''.join(ans))