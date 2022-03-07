import string

noraltext = input()
secretstext = input()

output = ""
l = len(secretstext)
for idx, c in enumerate(noraltext):
    if c == " ":
        output += " "
        continue
    dist = ord(secretstext[idx%l])-ord('a')+1
    output += string.ascii_lowercase[ord(c)-ord('a')-dist]
print(output)