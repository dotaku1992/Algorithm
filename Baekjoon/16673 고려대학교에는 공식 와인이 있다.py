#kc + pcc
# c k p 순
c,k,p = map(int,input().split())
wine_cnt = [k*n+p*n*n for n in range(c+1)]
print(sum(wine_cnt))