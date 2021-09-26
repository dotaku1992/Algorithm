while True:
    num = input()
    if num == '0':
        break
    widthsum = 1
    for char in num:
        if char == '0':
            widthsum+=4
        elif char == '1':
            widthsum+=2
        else:
            widthsum+=3
    widthsum+=len(num)
    print(widthsum)