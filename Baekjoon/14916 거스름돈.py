n = int(input())
ismake = [0 for _ in range(100006)]
coincnt = [100000 for _ in range(100006)]

#init
ismake[2]=1
ismake[5]=1
coincnt[2]=1
coincnt[5]=1

for coinval in range(n+1):
    if ismake[coinval]:
        ismake[coinval+2]=1
        coincnt[coinval+2] = min(coincnt[coinval+2],coincnt[coinval]+1)
        ismake[coinval+5]=1
        coincnt[coinval + 5] = min(coincnt[coinval + 5], coincnt[coinval] + 1)
print(-1 if not ismake[n] else coincnt[n] )