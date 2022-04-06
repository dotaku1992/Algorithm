text = input()

arr = []
ans = 0
for idx, val in enumerate(text):
    if val == "(":
        arr.append((val, idx))
    else:
        if arr[-1][1] == idx - 1:  # 자르는행동
            ans += len(arr) - 1
        else:
            ans += 1
        arr.pop(-1)
print(ans)
