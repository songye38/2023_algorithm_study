def solution(numlist, n):
    gap_list = [[abs(i-n),i] for i in numlist]
    gap_list.sort(key= lambda x : (x[0], -x[1]))
    
    
        
    return [i[1] for i in gap_list]