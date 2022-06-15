# lv1
from itertools import combinations


def solution(nums):
    answer = 0
    isPrime = [1] * (1000 * 50 + 1)
    isPrime[1] = 0

    for val in range(2, 1000 * 50 + 1):
        if isPrime[val]:
            for mul in range(2, 1000 * 50 + 1):
                if mul * val > 1000 * 50:
                    break
                isPrime[val * mul] = 0

    for per in combinations(nums, 3):
        answer += isPrime[sum(per)]

    return answer
