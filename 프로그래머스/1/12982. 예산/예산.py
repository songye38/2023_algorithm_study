def solution(d, budget):
    d.sort()
    total_sum = 0
    count = 0
    for i in d:
        total_sum += i
        count +=1
        if total_sum > budget:
            return count-1
        
    return count