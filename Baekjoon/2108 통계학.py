import sys
import math
from collections import defaultdict
n = int(input())
arr = [int(sys.stdin.readline().rstrip()) for _ in range(n)]
arr.sort()

arr_sum = 0
check = defaultdict(int)
max_val_arr = []
for val in arr:
    arr_sum+=val
    check[val]+=1

max_cnt = max(check.values())
modes = [key for (key,val) in check.items() if val == max_cnt]
modes.sort()
print(f"{math.floor((arr_sum/n)+0.5)}\n{arr[n//2]}\n{modes[0] if len(modes)==1 else modes[1] }\n{arr[-1]-arr[0]}")
