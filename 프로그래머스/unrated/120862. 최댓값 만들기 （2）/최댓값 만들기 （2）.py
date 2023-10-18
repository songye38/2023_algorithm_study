from itertools import combinations
def solution(numbers):
    numbers = combinations(numbers,2)
    answer = [i*j for i,j in numbers]
    return max(answer)