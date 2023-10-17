import itertools

def check_prime(n):
    for i in range(2,n):
        if n % i ==0:
            return False
    return True
    
def solution(nums):
    answer = 0
    combi = [sum(i) for i in itertools.combinations(nums,3)]
    for i in combi:
        if check_prime(i):
            answer +=1 
    return answer