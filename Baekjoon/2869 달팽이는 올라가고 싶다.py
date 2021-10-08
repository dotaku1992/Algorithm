import math
a,b,v = map(int,input().split())
#a올라가고 b미끄러진다  a가 항상 b가 크니 무조건 정상에 도달할 수 있음
#t >= (v-b)/(a-b)
if a==v:
    print(1)
else:
    print(math.ceil((v-b)/(a-b)))
