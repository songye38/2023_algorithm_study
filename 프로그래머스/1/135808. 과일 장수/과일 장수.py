def solution(k, m, score):
    score.sort()
    answer = 0
    while len(score)>=m:
        answer += min(score[len(score)-m:]) * m
        del score[len(score)-m:]
    return answer