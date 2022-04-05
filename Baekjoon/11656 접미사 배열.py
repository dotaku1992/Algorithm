text = input()
text_arr = []

for idx,_ in enumerate(text):
    text_arr.append(text[idx:])
text_arr.sort()
for val in text_arr:
    print(val)