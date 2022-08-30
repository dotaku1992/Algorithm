T = int(input())
# bmi = 체중 / 신장

for _ in range(T):
    tall, weight = map(int, input().split())
    if tall < 140.1:
        print(6)
    elif tall < 146:
        print(5)
    elif tall < 159:
        print(4)
    elif tall < 161:
        bmi = weight / ((tall / 100) ** 2)
        if 16 <= bmi < 35:
            print(3)
        else:
            print(4)

    elif tall < 204:
        bmi = weight / ((tall / 100) ** 2)
        if 20 <= bmi < 25:
            print(1)
        elif (18.5 <= bmi < 20) or (25.0 <= bmi < 30):
            print(2)
        elif (16 <= bmi < 18.5) or (30 <= bmi < 35):
            print(3)
        else:
            print(4)
    else:
        print(4)
