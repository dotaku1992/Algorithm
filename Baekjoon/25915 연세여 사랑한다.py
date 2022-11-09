import string

char = input()
ALPABET = string.ascii_uppercase
print(84 + abs(ALPABET.index('I') - ALPABET.index(char)))
