def solution(s):
    answer = []
    for char in s:
        if s.count(char) ==1:
            answer += char
    answer.sort()
    return "".join(answer)