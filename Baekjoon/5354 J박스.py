T = int(input())

for _ in range(T):
    n = int(input())
    str_arr = [['J' for i in range(n)] for j in range(n)]
    for y in range(n):
        for x in range(n):
            if x == 0 or y== 0 or x==n-1 or y==n-1:
                print('#',sep="",end='')
            else:
                print(str_arr[y][x],sep="",end='')
        print()
    print()