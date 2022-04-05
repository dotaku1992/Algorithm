import sys

n = int(sys.stdin.readline().rstrip())

dist = list(map(int,sys.stdin.readline().rstrip().split()))
arr = list(map(int,sys.stdin.readline().rstrip().split()))
cur_min = arr[0]
ans = 0
for idx,val in enumerate(arr):
    cur_min=min(cur_min,val)
    arr[idx]=cur_min

for dis,pri in zip(dist,arr):
    ans += dis*pri
print(ans)