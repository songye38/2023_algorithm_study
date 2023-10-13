def solution(rsp):
    answer = ''
    for type in rsp:
        if type=='2':
            answer += "0"
        elif type=='0':
            answer += "5"
        else:
            answer += "2"
    return answer