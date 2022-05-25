key, nomraltext = input(), input()
l = len(key)
fromidxarr = [[] for _ in range(l)]
for idx, c in enumerate(nomraltext):
    fromidxarr[idx // (len(nomraltext) // l)].append(c)
arr = []
for idx, c in enumerate(key):
    arr.append((c, idx))
arr.sort(key=lambda x: (x[0], x[1]))

newarr = [None for i in range(l)]
for idx, val in enumerate(arr):
    newarr[val[1]] = fromidxarr[idx]

ans = ''
for y in range(len(nomraltext) // l):
    for x in range(l):
        ans += newarr[x][y]
print(ans)
