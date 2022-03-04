from collections import defaultdict
arr = []
check = defaultdict(int)
for _ in range(10):
    inp = int(input())
    arr.append(inp)
    check[inp]+=1
mostcountedval = max(check.items(),key = lambda x:x[1])
print(f"{sum(arr)//10}\n{mostcountedval[0]}")