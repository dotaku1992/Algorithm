in1, in2 = map(int, input().split())
a, b = 100 - in1, 100 - in2
c, d = 100 - (a + b), a * b
q, r = divmod(d, 100)
print(a, b, c, d, q, r)
print(c + q, r)
