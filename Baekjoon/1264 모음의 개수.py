import sys

while True:
    text = sys.stdin.readline().rstrip().lower()
    if text == "#":
        break
    ans = 0
    for ele in text:
        if ele in ['a','e','i','o','u']:
            ans +=1
    print(ans)
