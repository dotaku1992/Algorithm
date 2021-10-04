from collections import defaultdict
n,m = map(int,input().split())
arr = []

for _ in range(n):
    input_text = input()
    arr.append(input_text)

ans = 1

for length in range(1,max(n,m)):
    for y in range(n):
        for x in range(m):
            if x+length<m and y +length<n:
                check = defaultdict(int)
                check[arr[y][x]]+=1
                check[arr[y+length][x]]+=1
                check[arr[y][x+length]]+=1
                check[arr[y+length][x+length]]+=1
                if len(check)==1:
                    ans=max(ans,(length+1)**2)
print(ans)