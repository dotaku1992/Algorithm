hash = [None, "January", "February", "March", "April", "May", "June", "July", "August", "September", "October",
        "November", "December"]
days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
md, ytime = input().split(',')
m, d = md.split()
y, hs = ytime[1:].split()
days[2] = days[2] + (int(y) % 400 == 0 or (int(y) % 4 == 0 and int(y) % 100 != 0))
h, s = hs.split(':')

numerator = (sum(days[:hash.index(m)]) + int(d) - 1) * 24 * 60 * 60 + int(h) * 60 * 60 + int(s) * 60
denominator = sum(days) * 24 * 60 * 60

print(f"{numerator / denominator * 100.0:0.9f}")
