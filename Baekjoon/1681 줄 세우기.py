n,l = map(int,input().split())
cnt = 0
num = 1
while True:
    if str(l) not in str(num):
        cnt+=1
    if cnt == n:
        break
    num+=1
print(num)
