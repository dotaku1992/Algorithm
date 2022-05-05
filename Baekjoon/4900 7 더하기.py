convert = {0b0111111: 0,
             0b0001010: 1,
             0b1011101: 2,
             0b1001111: 3,
             0b1101010: 4,
             0b1100111: 5,
             0b1110111: 6,
             0b0001011: 7,
             0b1111111: 8,
             0b1101011: 9}
#test
convert2 = {val : key for key ,val in convert.items()}

def change(input_text : str):
    output = ''
    for idx in range(0,len(input_text),3):
        output+=str(convert[int(input_text[idx:idx+3])])
    return int(output)

def change2(int_num : int):
    strnum = str(int_num)
    output = ''
    for val in strnum:
        t = convert2[int(val)]
        t = str(t)
        output+=('0'*(3-len(t))+t)
    return output


while(True):
    text = input()
    if text == "BYE":
        break

    a,b = text.split('+')
    b = b[:-1]
    ans = change(a)+change(b)
    print(f"{a}+{b}={change2(ans)}")