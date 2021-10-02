while True:
    text = input()
    if text=="0":
        break
    while(len(text)!=1):
        sumele = 0
        for ele in text:
            sumele+=int(ele)
        text = str(sumele)
    print(text)