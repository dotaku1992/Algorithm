ans = []

def div(val):
    if val == 1:
        return
    else:
        for den in range(2,val+1):
            if val%den==0:
                ans.append(den)
                div(val//den)
                break

num = int(input())
div(num)
for ele in ans:
    print(ele)
