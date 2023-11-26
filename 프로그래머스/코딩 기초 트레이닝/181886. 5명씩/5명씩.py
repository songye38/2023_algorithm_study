def solution(names):
    answer =[]
    #if len(names)==5:
    #    return names[0]
    
    for i in range(len(names)//5):
        answer.append(names[i * 5])
    if len(names)%5==0:
        return answer
    else:
        answer.append(names[(len(names)//5) * 5])
        return answer