import sys
wm,bm = map(int,sys.stdin.readline().rstrip().split())
ws,bs = map(int,sys.stdin.readline().rstrip().split())
wp,bp = map(int,sys.stdin.readline().rstrip().split())
a,b = min(wm,bs,wp),min(bm,ws,bp)
print(2*min(a,b) + int(a!=b))