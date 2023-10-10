def solution(absolutes, signs):
    signs = [1 if i == True else -1 for i in signs]
    sum = 0
    for i in range(len(absolutes)):
        sum += absolutes[i] * signs[i]
    return sum