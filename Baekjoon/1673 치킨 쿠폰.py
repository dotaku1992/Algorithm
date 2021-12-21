while True:
    try:
        n,k = map(int,input().split())
        ans = n
        while n >= k:
            chik = n//k
            ans+=chik
            n = n//k + n%k
        print(ans)

    except:
        break