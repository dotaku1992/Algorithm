import sys

convert = {
    'NLCS': 'North London Collegiate School',
    'BHA': 'Branksome Hall Asia',
    'KIS': 'Korea International School',
    'SJA': 'St. Johnsbury Academy'
}
text = sys.stdin.readline().rstrip()
print(convert[text])
