from collections import defaultdict

sinario=1
while True:
    n = int(input())
    names =defaultdict(str)
    cnt = defaultdict(int)
    if n:
        for no in range(n):
            names[no+1] = input()
        for i in range(2*n-1):
            idx,_ =input().split()
            cnt[int(idx)]+=1
        for (key,value) in cnt.items():
            if value == 1:
                print(f"{sinario} {names[int(key)]}")
                sinario+=1
    else : break