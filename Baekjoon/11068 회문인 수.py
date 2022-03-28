import string

convert = "0123456789" + string.ascii_uppercase + string.ascii_lowercase +"+-"


def digit10ToN(num: int, digit: int) -> str:
    output = ""
    while num:
        output += convert[num % digit]
        num //= digit
        if n == 0:
            break
    return output


def isPalindrome(text: str):
    return text == text[::-1]


T = int(input())

for _ in range(T):
    num = int(input())
    Palindromeflag = False
    for n in range(2, 65):
        Palindromeflag = isPalindrome(digit10ToN(num, n))
        if Palindromeflag:
            break
    print(1 if Palindromeflag else 0)
