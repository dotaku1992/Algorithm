def solution(n):
    digit3str = ''
    while (True):
        if n == 0:
            break
        digit3str += str(n % 3)
        n //= 3
    answer = sum([int(v) * (3 ** e) for e, v in enumerate(digit3str[::-1])])

    return answer
