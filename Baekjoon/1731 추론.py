n = int(input())
arr = []
for _ in range(n):
    arr.append(int(input()))

sum_arithmetic = n*(arr[0]+arr[-1])//2
if sum_arithmetic == sum(arr):
    print(arr[-1]+arr[1]-arr[0])
else:
    print(arr[-1]*(arr[1]//arr[0]))
