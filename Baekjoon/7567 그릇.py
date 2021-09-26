plate = input()
ans = 10
for idx in range(1,len(plate)):
    if plate[idx] == plate[idx-1]:
        ans+=5
    else:
        ans+=10
print(ans)
