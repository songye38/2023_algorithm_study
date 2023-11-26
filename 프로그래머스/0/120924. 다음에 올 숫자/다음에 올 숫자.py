def solution(common):
    temp = []
    for i in range(len(common)-1):
        temp.append(common[i+1]-common[i])
    if max(temp)== min(temp):
        return common[-1] + temp[0]
    else:
        return common[-1] * (common[-1] /common[-2])