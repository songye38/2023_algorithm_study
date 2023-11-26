def solution(s1, s2):
    answer = 0
    shorter_s = 0
    longer_s = 0
    if len(s1) <= len(s2):
        shorter_s = s1
        longer_s = s2
    else:
        shorter_s = s2
        longer_s = s1
    for i in range(len(shorter_s)):
        if shorter_s[i] in longer_s:
            answer +=1
    return answer
            
        