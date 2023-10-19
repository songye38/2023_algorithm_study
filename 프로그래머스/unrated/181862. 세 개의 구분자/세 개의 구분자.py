def solution(myStr):
    answer = []
    for i in myStr:
        if i !='a' and i !='b' and i !='c':
            answer.append(i)
        else:
            answer.append(' ')
    answer = "".join(answer).split()
    if answer :
        return answer
    else:
        return ['EMPTY']