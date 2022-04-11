while (True):
    n = int(input())
    if not n: break

    infos = []
    for _ in range(n):
        name, tall = input().split()
        infos.append((name, float(tall)))
    maxtall = max(infos, key=lambda x: x[1])[1]
    ans = []
    for name, tall in infos:
        if tall == maxtall:
            ans.append(name)
    print(' '.join(ans))
