from collections import defaultdict
while True:
    arr = list(map(int,input().split()))
    if arr[0]==arr[1]==arr[2]==0:
        break
    check_cnt = defaultdict(int)
    arr.sort()
    check_cnt[arr[0]]+=1
    check_cnt[arr[1]]+=1
    check_cnt[arr[2]]+=1
    for_print = ['Equilateral','Isosceles','Scalene']
    
    if arr[2]<arr[1]+arr[0]:
        print(for_print[len(check_cnt)-1])
    else:
        print('Invalid')

