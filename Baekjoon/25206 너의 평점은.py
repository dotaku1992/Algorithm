hakarr = []
gradearr = []
gradetoint = {'A+': 4.5, 'A0': 4.0, 'B+': 3.5, 'B0': 3.0, 'C+': 2.5, 'C0': 2.0, 'D+': 1.5, 'D0': 1.0, 'F': 0.0}
for _ in range(20):
    classname, hak, grade = input().split()
    if grade == 'P':
        continue
    hakarr.append(float(hak))
    gradearr.append(float(gradetoint[grade]))
print(f'{(sum([h * g for h, g in zip(hakarr, gradearr)]) / (sum(hakarr))):.5f}')
