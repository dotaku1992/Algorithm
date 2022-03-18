arr = []
while (data :=float(input())) != 999:
    arr.append(data)
for idx,_ in enumerate(arr[1:],1):
    print(f"{(arr[idx]-arr[idx-1]):.2f}")