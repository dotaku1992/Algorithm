import sys
N = int(sys.stdin.readline().rstrip())
print('int a;')
print('int *ptr = &a;')
for i in range(2,N+1):
    print(f'int {"*"*i}ptr{i} = &ptr{"" if i==2 else i-1};')