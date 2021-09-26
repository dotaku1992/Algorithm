t = int(input())

for _ in range(t):
    n,k = map(int,input().split())
    candy_arr = list(map(int,input().split()))
    for idx in range(n):
        candy_arr[idx] = candy_arr[idx]//k
    print(sum(candy_arr))