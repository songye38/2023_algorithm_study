def solution(order):
    answer =0
    for char in str(order):
        if char=='3' or char=='6' or char=='9':
            answer += 1
    return answer