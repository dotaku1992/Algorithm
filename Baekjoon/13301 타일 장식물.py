n = int(input())
arr = [0 for _ in range(81)]
arr[2] = arr[1] = 1

for i in range(3, 81):
    arr[i] = arr[i - 1] + arr[i - 2]
if n == 1:
    print(4)
elif n == 2:
    print(6)
else:
    print(2 * (arr[n] + arr[n - 1] + arr[n - 1] + arr[n - 2]))
