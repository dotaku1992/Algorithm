n = int(input())
names = [input() for _ in range(n)]

prev_text = names[0]
is_increasing = True
is_decreasing = True
for name in names:
    is_increasing &= (prev_text <= name)
    is_decreasing &= (prev_text >= name)
    prev_text = name

if is_increasing == False and is_decreasing == False:
    print("NEITHER")
else:
    print("INCREASING" if is_increasing else "DECREASING")
