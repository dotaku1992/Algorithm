from collections import defaultdict

while True:
    try:
        a, b = map(int, input().split())
        ans = 0
        for i in range(a, b + 1):
            numtostr = str(i)
            check = defaultdict(int)
            for c in numtostr:
                check[c] += 1
            flag = True
            for cnt in check.values():
                if cnt > 1:
                    flag = False
            ans += flag
        print(ans)

    except:
        break