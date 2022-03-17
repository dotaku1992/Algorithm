isprime = [1]*(52*20+1)
for val in range(2,52*20+1):
    if isprime[val] ==1:
        for nval in range(val*2,50*20+1,val):
            isprime[nval]=0

text = input()
ans = 0

for c in text:
    if c.islower():
        ans +=ord(c)-ord('a')+1
    else:
        ans +=ord(c)-ord('A')+27
print(ans)
print("It is a prime word." if isprime[ans] else "It is not a prime word.")
