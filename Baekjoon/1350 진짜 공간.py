import math

n = int(input())
arr = list(map(int, input().split()))
memory = int(input())
ans = [math.ceil(arr[i] / memory) for i in range(n)]
print(int(sum(ans)) * memory)