def solution(hp):
    answer = 0
    for power in [5,3,1]:
        answer += hp // power
        hp = hp %power
    return answer