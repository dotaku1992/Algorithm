n = int(input())

for _ in range(n):
    text = input()
    print((text[0].upper()+(text[1:] if len(text)!=0 else "")))
