while True:
    text = input()
    if text == '0':
        break
    while len(text)!= 1:
        sub_ans =0
        for ch in text:
            sub_ans += int(ch)
        text = str(sub_ans)
    print(text)