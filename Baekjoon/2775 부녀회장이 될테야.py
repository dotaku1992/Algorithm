#a층 b호에 살려면 a-1층의 1~b호까지 사람들으 ㅣ수의 합만큼 사람들을 데려와 살야아한다.
#비어있는집은 없고 모두 계약 조건을 지킨다.
#아파트는 0층부터 있고 1호부터 있다.
t = int(input())

for _ in range(t):
    k = int(input())
    n = int(input())
    arr = [i for i in range(1,n+1)]
    for _ in range(k):
        sub_arr = [sum(arr[0:i]) for i in range(1,n+1)]
        arr = sub_arr
    print(arr[n-1])
