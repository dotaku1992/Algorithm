x, y, xyprice, crossprice = map(int, input().split())
if xyprice * 2 <= crossprice:
    print(xyprice * (x + y))
else:
    ans = min(x, y) * crossprice
    leftdist = max(y - min(x, y), x - min(x, y))
    ans += min((leftdist // 2) * 2 * xyprice, (leftdist // 2) * 2 * crossprice)
    ans += min((leftdist % 2) * xyprice, (leftdist % 2) * (xyprice + crossprice))
    print(ans)
'''
문제를 해설해보자면 이동해야하는 거리 x,y가 있을때 x,y 둘중 최소값은 가로질러 가던 x방향->y방향 두차례로 이동하는 방향에서 최소이동거리를 구한다
그렇게 되면 이제 이동한 위치를 distmin이라 했을때 x,y는 distmin,distmin 동일한 위치를 가지게 되고 이 위치에서 goal목적지까지는 일직선이다.
일직선일 경우에 2칸씩 이동한다 했을때 대각선이동과 평행이동은 동일한 위치를 가지게 된다. 하지만 홀수일경우에는 대각선이동은 대각선 이후에 평행이동을 한번해준 것과 비교를 해야한다.
즉 코드상에 7번줄이 2칸씩 이동했을때(평행이동이나 대각선이동이나 끝부분이 동일한위치)에서 최소값을 더하고
8번줄은 만약 goal까지의 거리가 홀수 일경우에는 leftdist%2 에서 1이 나오게 될것이고 1인 경우에는 대각방향의 이동을 goal보다 항상 x방향이던 y방향이던 거리가 1이 차이가 나기에 무조건 한번 평행이동을 해줘야하고 그 비용까지 계산해야한다.
하지만 평행이동인 경우에는 그저 한칸 움직인것과 비교해서 최소값을 더해주면 된다.
짝수인경우 0 이 나올것이라 무조건 0이 더해질것이라 계산을 안한것처럼 효과를 낼 수 있다.
'''
