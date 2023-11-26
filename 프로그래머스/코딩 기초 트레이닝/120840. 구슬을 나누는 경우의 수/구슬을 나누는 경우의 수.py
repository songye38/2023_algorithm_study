from itertools import combinations

def factorial(n):
    result = 1
    for i in range(1,n+1):
        result *= i 
    return result

def solution(balls, share):
    answer = factorial(balls) / (factorial(balls-share) * factorial(share))
    return answer