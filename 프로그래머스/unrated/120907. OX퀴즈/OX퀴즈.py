def solution(quiz):
    answer = []
    for i in range(len(quiz)):
        temp = quiz[i].split()
        if temp[1]=='+':
            total = int(temp[0]) + int(temp[2])
            if total == int(temp[4]):
                answer.append('O')
            else:
                answer.append('X')
        else:
            minus =  int(temp[0]) - int(temp[2])
            if minus == int(temp[4]):
                answer.append('O')
            else:
                answer.append('X')
    return answer
        