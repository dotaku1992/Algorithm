check = [0 for i in range(31)]
for _ in range(28):
    check[int(input())]=1
for idx in range(1,31):
    if not check[idx]:
        print(idx)
