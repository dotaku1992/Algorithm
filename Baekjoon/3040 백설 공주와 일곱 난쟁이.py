arr = []
for _ in range(9):
    arr.append(int(input()))

for i in range(0,1<<9):
    truecnt = 0
    for j in range(9):
        truecnt += bool(i & (1<<j))
    if truecnt == 7:
        scoresum = 0
        for j in range(9):
            scoresum +=arr[j]*(bool(i & (1<<j)))
        if scoresum == 100:
            for j in range(9):
                if (i & (1<<j)):
                    print(arr[j])