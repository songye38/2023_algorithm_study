import re
def max_index(s,target):
    return max([m.start() for m in re.finditer(target, s)])
def solution(s):
    index_list = []
    answer = []
    for i in range(len(s)):
        if s[i] not in index_list:
            index_list.append(s[i])
            answer.append(-1)
        else:
            answer.append(i - max_index(s[:i],s[i]))    
    return answer