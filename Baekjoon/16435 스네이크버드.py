n,snake_len = map(int,input().split())
height = list(map(int,input().split()))
height.sort()

for ele in height:
    if ele <=snake_len:
        snake_len+=1
    else: break

print(snake_len)