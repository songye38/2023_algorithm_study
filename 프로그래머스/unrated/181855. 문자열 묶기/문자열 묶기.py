def solution(strArr):
    answer = [[] * 1 for i in range(31)]
    for i in strArr:
        answer[len(i)].append(i)
    answer = [len(i) for i in answer if i]
    return max(answer)