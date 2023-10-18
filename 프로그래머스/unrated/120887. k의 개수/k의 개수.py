def solution(i, j, k):
    answer = [0] * 10
    for num in range(i,j+1):
        for n in list(str(num)):
            answer[int(n)] +=1
    return answer[k]
            
        