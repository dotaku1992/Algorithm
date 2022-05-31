import sys

text = sys.stdin.readline().rstrip()
trycnt = 0
while (len(text) > 1):
    sumval = 0
    trycnt += 1
    for ele in text:
        sumval += int(ele)
    text = str(sumval)

print(f"{trycnt}\n{'NO' if int(text) % 3 else 'YES'}")
