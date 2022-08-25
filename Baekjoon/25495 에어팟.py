n = int(input())
arr = [x for x in input().split()]
sumarr = [0 for _ in range(n)]
Battery = 0
curid, sumarr[0] = None, 2

for idx, id in enumerate(arr):
    if id == curid:
        sumarr[idx] = sumarr[idx - 1] * 2
    else:
        sumarr[idx] = 2
    curid = id
    if Battery + sumarr[idx] >= 100:
        sumarr[idx] = 0
        Battery = 0
        curid = None
    Battery += sumarr[idx]

print(Battery)
