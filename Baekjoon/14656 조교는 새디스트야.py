n = int(input())

stu_list = list(map(int,input().split()))
for idx in range(n):
    if stu_list[idx]==idx+1:
        n-=1
print(n)
