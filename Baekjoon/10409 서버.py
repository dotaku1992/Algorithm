n,t = map(int,input().split())
input_list = list(map(int,input().split()))
cnt = 0
for ele in input_list:
    t-=ele
    if t<=0:
        break
    else:
        cnt+=1
print(cnt)