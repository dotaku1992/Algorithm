import sys

person = list(sys.stdin.readline().rstrip().split() for _ in range(3))


def firstmethod(data):
    sortedDatawithfirst = sorted(data, key=lambda x: int(x[1]) % 100)
    output = ''
    for _, sec, _ in sortedDatawithfirst:
        output += str(int(sec) % 100)
    return output


def secondmethod(data):
    sortedDatawithsecond = sorted(data, key=lambda x: -int(x[0]))
    output = ''
    for _, _, name in sortedDatawithsecond:
        output += name[0]
    return output


print(firstmethod(person))
print(secondmethod(person))
