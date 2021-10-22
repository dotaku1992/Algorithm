n = int(input())
text = input()
print("A" if text.count('A') > text.count('B') else "Tie" if text.count('A')==text.count('B') else 'B')