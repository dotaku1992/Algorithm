from collections import defaultdict
s1,s2,s3 = map(int,input().split())
cnt = defaultdict(int)
for n1 in range(1,s1+1):
    for n2 in range(1,s2+1):
        for n3 in range(1,s3+1):
            cnt[n1+n2+n3]+=1
max_cnt=0
min_sum=10000
for key,value in cnt.items():
    if value > max_cnt:
        max_cnt = value
        min_sum = key
    elif value == max_cnt and min_sum > key:
        min_sum = key
    else:
        pass
print(min_sum)