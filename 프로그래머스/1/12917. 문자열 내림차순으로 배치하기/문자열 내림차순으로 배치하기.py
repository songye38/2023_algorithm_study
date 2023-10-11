def solution(s):
    answer = []
    for i in range(len(s)):
        answer.append((-ord(s[i]),s[i]))
    answer.sort(key=lambda answer : answer[0])
    return "".join([i[1] for i in answer])