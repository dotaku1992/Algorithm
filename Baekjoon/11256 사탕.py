T = int(input())

for _ in range(T):
    candy,boxn = map(int,input().split())
    boxs = []
    for _ in range(boxn):
        h,w = map(int,input().split())
        boxs.append(h*w)
    boxs.sort(reverse=True)
    ans = 0
    sumboxarea=0
    for area in boxs:
        ans+=1
        sumboxarea+=area
        if sumboxarea >=candy:
            break
    print(ans)