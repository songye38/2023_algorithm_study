def solution(price, money, count):
    answer = [i * price for i in range(1,count+1)]

    if money > sum(answer):
        return 0
    else:
        return sum(answer) - money