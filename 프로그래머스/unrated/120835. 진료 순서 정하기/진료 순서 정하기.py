def solution(emergency):
    new_array = sorted(emergency.copy(),reverse=True)
    answer = []
    for i in emergency:
        answer.append(new_array.index(i)+1)
    return answer