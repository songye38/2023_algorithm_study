from fractions import Fraction
def solution(numer1, denom1, numer2, denom2):
    for i in range(max(denom1,denom2),(denom1*denom2)+1):
        if i % denom1 == 0 and i % denom2 == 0:
                temp = Fraction(numer1 * int(i / denom1) + numer2 * int(i / denom2), i)
                return [temp.numerator,temp.denominator]