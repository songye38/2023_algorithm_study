import itertools
def solution(number):
    answer = 0 #카운트하기 
    nPr = itertools.combinations(number, 3)
    for a,b,c in nPr:
        if a+b+c == 0:
            answer +=1
    return answer