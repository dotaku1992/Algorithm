t = int(input())

for case in range(t):
    arr = list(map(int, input().split()))
    arr = arr[1:]
    arr.sort()
    gap = -1
    for idx,_ in enumerate(arr[:-1]):
        gap = max(gap,arr[idx+1]-arr[idx])
    print(f"Class {case+1}\nMax {max(arr)}, Min {min(arr)}, Largest gap {gap}")
