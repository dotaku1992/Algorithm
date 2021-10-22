n = int(input())

cnt_alphbet = [0 for _ in range(ord('z')-ord('a')+1)]
for _ in range(n):
    text = input()
    cnt_alphbet[ord(text[0])-ord('a')]+=1

ans = [chr(ord('a')+idx) for idx,ele in enumerate(cnt_alphbet) if ele >=5]
print("PREDAJA" if not ans else ''.join(ans))