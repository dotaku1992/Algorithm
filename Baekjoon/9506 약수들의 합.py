def get_measure(n):
    return [i for i in range(1,n) if n%i==0]

while True:
    n = int(input())
    if n ==-1:
        break
    ans = get_measure(n)
    if n != sum(ans):
        print(f"{n} is NOT perfect.")
    else:
        print(f"{n} = {' + '.join(map(str,ans))}")