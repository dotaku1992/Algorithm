text = input()


def mult(arr):
    ans = 1
    for ele in arr:
        ans *= int(ele)
    return ans


is_yujinnum = False

for idx in range(len(text)):
    l, r = mult(text[0:idx + 1]), mult(text[idx + 1:len(text)])
    if l == r:
        is_yujinnum = True
        break
if len(text)==1:
    is_yujinnum=False
print("YES" if is_yujinnum else "NO")