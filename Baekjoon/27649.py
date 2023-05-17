import sys
import re

patten = re.compile('<|>|&&|\|\||\(|\)| ')
# 정규식에서 메타문자 사용하는방법 ->: \(백슬래시를 사용)
input_text = sys.stdin.readline().rstrip()
idx = 0
tokkens = []
while True:
    isMatch = patten.search(input_text, idx)
    if not isMatch:  # None이 나오는 경우 즉 일치하는 구분자가 없을때
        tokkens.append(input_text[idx:])
        break
    else:
        sidx, eidx = patten.search(input_text, idx).span()
        tokkens.append(input_text[idx:sidx])
        tokkens.append(input_text[sidx:eidx])
        idx = eidx
pretreatment_tokken = [tokken for tokken in tokkens if tokken and tokken != ' ']
print(' '.join(pretreatment_tokken))
