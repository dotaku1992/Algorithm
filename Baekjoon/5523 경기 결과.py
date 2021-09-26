import sys
n = int(input())
a_cnt,b_cnt = 0,0
for _ in range(n):
    a,b = map(int,sys.stdin.readline().rstrip().split())
    a_cnt +=(a>b)
    b_cnt +=(a<b)
print(a_cnt,b_cnt)