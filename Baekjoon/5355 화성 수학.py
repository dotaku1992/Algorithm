t = int(input())

def oper(val,op):
    if op =='@':
        return val*3
    elif op =='%':
        return val + 5
    elif op == '#':
        return val-7
    else:
        return val
for _ in range(t):
    arr = input().split()
    arr[0]=float(arr[0])
    val = arr[0]
    for ele in arr:
        val = oper(val,ele)
    print(f"{val:.2f}")

