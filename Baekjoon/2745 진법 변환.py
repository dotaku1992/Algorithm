fordictlist = [str(i) for i in range(10)]+[chr(i) for i in range(ord('A'),ord('Z')+1)]
arr = {ch : val for val,ch in enumerate(fordictlist)}
text,digit = input().split()
text,digit = text[::-1],int(digit)
ans = 0
for expo,ch in enumerate(text):
    ans += arr[ch]*digit**expo
print(ans)