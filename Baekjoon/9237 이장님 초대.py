import sys
n = int(input())
arr = list(map(int,sys.stdin.readline().rstrip().split()))
arr.sort(reverse=True)
ans = 0
for idx,ele in enumerate(arr,1):
    ans = max(ans,idx+ele)
print(ans+1) #다 자란후 다음날이므로 +1