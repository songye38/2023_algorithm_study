def solution(s):
    answer = ''
    result = [int(i) for i in s.split()]
    min_val = min(result)
    max_val = max(result)
    return str(min_val) + " "+str(max_val)