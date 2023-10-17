def get_divisor(n):
    answer =0
    for i in range(1, int(n**(1/2)) + 1): 
        if (n % i == 0):            
            answer +=1
            if (i != (n // i)): 
                answer += 1

    return answer


def solution(number, limit, power):
    answer = 0
    get_list = [get_divisor(i) for i in range(1,number+1)]
    for i in get_list:
        if i > limit:
            answer += power
        else:
            answer += i
    return answer