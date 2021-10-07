while True:
    text = input()
    if text=='0':
        break
    n,*arr = text.split()
    n = int(n)
    arr = list(map(int,arr))

    ans = 1;
    for idx in range(n):
        ans = ans*arr[2*idx]-arr[2*idx+1]
    print(ans)