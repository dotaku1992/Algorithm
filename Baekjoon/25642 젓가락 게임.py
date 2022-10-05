import sys

players = list(map(int,sys.stdin.readline().rstrip().split()))
playersName = ['yt','yj']
idx = 0
while True:
    if players[idx%2]>=5:
        break
    players[(idx+1)%2] += players[idx%2]
    idx+=1
print(playersName[(idx+1)%2])