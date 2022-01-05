T = int(input())

for _ in range(T):
    b1,b2 = input().split()
    max_size = max(len(b1),len(b2))
    b1_arr = ([0 for i in range(max_size-len(b1))] + [int(i) for i in b1])[::-1]
    b2_arr = ([0 for i in range(max_size-len(b2))] + [int(i) for i in b2])[::-1]
    b3_arr = ([0]* (max_size+1))[::-1]

    for idx, (v1,v2,v3) in enumerate(zip(b1_arr,b2_arr,b3_arr)):
        calu = v1+v2+v3
        b3_arr[idx]=calu%2
        b3_arr[idx+1]=calu//2

    if b3_arr.count(1)==0:
        print(0)
    else:
        while not b3_arr[-1]:
            b3_arr.pop()
        print(''.join(map(str,b3_arr[::-1])))
