p,k = map(int,input().split())
#k 범위 내에서의 소수가 있는지 여부만 확인하면 될것 같다. p는 우선 두소수의 곱인 값이라 명시가 되어 있으니
isPrime = [0 if i %2 == 0 else 1 for i in range(10**6)]
isPrime[1]=0
isPrime[2]=1
for val in range(2,k):
    if isPrime[val]:
        mul = 2
        while val*mul < k:
            isPrime[val*mul]=0
            mul+=1
flag = True
for i in range(2,k):
    if isPrime[i] and p%i==0:
        v1,v2 = i,p//i
        flag = False
print("GOOD" if flag else f"BAD {min(v1,v2)}")
