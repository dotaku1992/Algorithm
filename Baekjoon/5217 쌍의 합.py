n = int(input())

for idx in range(n):
    num = int(input())
    ans = [ f"{i} {num-i}" for i in range(1,n) if i < num-i]
    print(f"Pairs for {num}: ",end='')
    output = ', '.join(ans)
    print(output)