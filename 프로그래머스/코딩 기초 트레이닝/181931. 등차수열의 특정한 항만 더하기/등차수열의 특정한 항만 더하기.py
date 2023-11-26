def solution(a, d, included):
    sum = 0
    seq = [i for i in range(a,a+len(included)*d,d)]
    for i in range(len(included)):
        if included[i] == True:
            sum += seq[i]
    return sum