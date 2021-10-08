def sol(n):
    rank = 1
    while True:
        if rank >= n:
            l,r = (1,rank) if rank%2==0 else (rank,1)
            step = n-1
            l,r = (l+step,r-step) if rank%2==0 else (l-step,r+step)
            print(f"{l}/{r}")
            break
        else:
            n-=rank
            rank+=1

num = int(input())
sol(num)