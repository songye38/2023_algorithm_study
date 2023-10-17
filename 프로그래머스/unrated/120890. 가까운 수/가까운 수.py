def solution(array, n):
    array.sort()
    gap_list = [abs(i-n) for i in array]
    gap_val = min(gap_list)
    index = gap_list.index(gap_val)
    
    return array[index]