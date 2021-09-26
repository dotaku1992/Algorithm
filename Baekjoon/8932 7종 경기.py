t = int(input())
A = [9.23076,1.84523,56.0211,4.99087,0.188807,15.9803,0.11193]
B = [26.7,75,1.5,42.5,210,3.8,254]
C = [1.835,1.348,1.05,1.81,1.41,1.04,1.88]

for _ in range(t):
    P = list(map(int,input().split()))
    track_score = 0
    filed_score = 0
    for idx in range(len(P)):
        if idx in [0,3,6]:
            track_score += int( A[idx]*((B[idx]-P[idx])**C[idx]) )
        else:
            filed_score += int( A[idx]* ((P[idx]-B[idx])**C[idx]))
    print(track_score+filed_score)