N,W,H,L = map(int,input().split())
maxW = W//L
maxH = H//L
print(min(maxW*maxH,N))