def solution(cards1, cards2, goal):
    answer = True
    c1_index = 0
    c2_index = 0
    for word in goal:
        if c1_index < len(cards1) and cards1[c1_index]==word:
            c1_index +=1
        elif c2_index < len(cards2) and cards2[c2_index]==word:
            c2_index += 1
        else:
            return "No"
    return "Yes"