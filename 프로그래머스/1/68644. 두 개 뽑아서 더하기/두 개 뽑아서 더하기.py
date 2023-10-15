from itertools import combinations
def solution(numbers):
    answer = set()
    answers = combinations(numbers,2)
    for num1,num2 in answers:
        answer.add(num1+num2)
    answer = list(answer)
    answer.sort()
    return answer