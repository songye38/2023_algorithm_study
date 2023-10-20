def solution(M, N):
    answer = [0,0]
    if M==1 and N==1:
        return 0
    
    answer[0] = M-1
    answer[1] = (N-1)*M
    
    return answer[0] + answer[1]