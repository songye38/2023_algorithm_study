import math
def solution(n):
    sqrt_n = math.sqrt(n)
    if (math.modf(sqrt_n))[0] !=0:
        return -1
    else:
        return (math.sqrt(n)+1) ** 2