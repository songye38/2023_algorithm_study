from fractions import Fraction

def get_factorint(n):
    d = 2
    answer = []
    while d <= n:
        if n%d==0:
            answer.append(d)
            n = n / d
        else:
            d +=1
    return answer
            

def solution(a, b):
    a = Fraction(a,b) #numerator,denominator
    answer = list(set(get_factorint(a.denominator)))
    if 2 in answer:
        answer.remove(2)
    if 5 in answer:
        answer.remove(5)
    
    if not answer:
        return 1
    else:
        return 2