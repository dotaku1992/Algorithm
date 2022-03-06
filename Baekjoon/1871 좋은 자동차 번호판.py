def first_price(text: str):
    output = 0
    for e, c in enumerate(text[::-1]):
        output += (ord(c) - ord('A')) * 26 ** e
    return output


n = int(input())

for _ in range(n):
    first, second = input().split('-')
    print("nice" if abs(first_price(first) - int(second)) <= 100 else "not nice")
