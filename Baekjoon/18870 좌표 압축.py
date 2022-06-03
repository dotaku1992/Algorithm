import sys
from collections import defaultdict

n = int(sys.stdin.readline().rstrip())
arr = list(map(int, sys.stdin.readline().rstrip().split()))
sorted_arr = sorted(arr)
checkorder = defaultdict(int)  # key : num , value : orderNo
no = 0
for val in sorted_arr:
    if val not in checkorder:
        checkorder[val] = no
        no += 1

for val in arr:
    print(checkorder[val], end=' ')
print()
