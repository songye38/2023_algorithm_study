
import re
def solution(s):
    result = {}
    answer = []
    s = list(s)
    s[0] = ""
    s[-1] = ""
    s = "".join(s)
    s = re.findall(r'\{(\d+(?:,\d+)*)\}', s)
    s = [i.split(',') for i in s]
    for i in s:
        result[len(i)] = i
    for i in range(1,len(s)+1):
        for j in result[i]:
            if int(j) not in answer:
                answer.append(int(j))
    return answer