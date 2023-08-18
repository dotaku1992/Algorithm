import sys

my, mm, md = map(int, sys.stdin.readline().rstrip().split('-'))

cnt = 0
for _ in range(int(sys.stdin.readline().rstrip())):
    iy, im, id = map(int, sys.stdin.readline().rstrip().split('-'))
    arr = []
    for m, i in zip([my, mm, md], [iy, im, id]):
        result = 1 if i > m else 0 if i == m else -1
        arr.append(result)
    flag = False
    for ele in arr:
        flag = (ele == 1) | flag
        if ele == 0 or ele == 1:
            continue
        else:
            if flag:
                continue
            else:
                break
    else:
        cnt += 1
print(cnt)
