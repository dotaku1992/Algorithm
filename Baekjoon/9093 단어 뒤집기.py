t= int(input())
for _ in range(t):
    str_arr = list(input().split())
    for text in str_arr:
        print(text[::-1],end=' ')