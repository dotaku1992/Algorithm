def solution(price, money, count):
    answer = max((count*(price+price*count))//2-money,0)
    return answer