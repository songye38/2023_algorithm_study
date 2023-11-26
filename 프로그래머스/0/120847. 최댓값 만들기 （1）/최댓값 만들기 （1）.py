from itertools import combinations
def solution(numbers):
    answer = 0
    combi_list = combinations(numbers,2)
    for a,b in combi_list:
        if answer < a * b:
            answer = a * b 
    return answer