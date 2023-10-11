def solution(numbers):
    set1 = set(numbers)
    set2 = set([i for i in range(10)])
    return sum(list(set2-set1))