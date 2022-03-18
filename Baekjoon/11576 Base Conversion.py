import sys
A,B = map(int,input().split())
m = int(input())
arr = list(map(int,sys.stdin.readline().rstrip().split()))

convertto10digit = 0
ans = []
for exp,val in enumerate(arr[::-1],0):
    convertto10digit += val*A**exp

while True:
    ans.append(convertto10digit%B)
    convertto10digit = convertto10digit//B
    if convertto10digit: continue
    break
print(' '.join(map(str,ans[::-1])))

