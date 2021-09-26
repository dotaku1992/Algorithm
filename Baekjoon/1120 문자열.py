small_text,big_text = input().split()

ans = max(len(small_text),len(big_text))

for pidx in range(len(big_text)-len(small_text)+1):
    diff_count = 0
    for sidx in range(len(small_text)):
        if small_text[sidx] != big_text[sidx+pidx]:
            diff_count+=1
    ans = min(ans,diff_count)
print(ans)