n = int(input())
a_cnt = 1
b_cnt = 0
for _ in range(n):
    a_cnt ,b_cnt = b_cnt,b_cnt+a_cnt
print(a_cnt, b_cnt)