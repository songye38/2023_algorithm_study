def solution(s):
    if s[0]==')':
        return False
    answer = []
    for i in s:
        if i =='(':
            answer.append(i)
        else:
            if answer:
                answer.pop()
    if answer:
        return False
    else:
        return True