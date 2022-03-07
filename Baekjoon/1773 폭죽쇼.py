# pypy로 제출하면 통과 python3 제출하면 시간초과
n, s = map(int, input().split())
arr = [0] * (s + 1)
for _ in range(n):
    sec = int(input())
    for t in range(sec, s + 1, sec):
        arr[t] = 1
print(sum(arr))
