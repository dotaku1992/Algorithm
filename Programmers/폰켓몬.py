def solution(nums):
    set_nums = set(nums)
    answer = min(len(nums) // 2, len(set_nums))
    return answer
