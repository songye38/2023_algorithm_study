def solution(A, B):
    if A ==B:
        return 0
    answer = ""
    i = 0
    count = 0 #몇번을 바꿨는지 카운트

    while i<100: #최대 100번까지 교체할 수 있다고 가정
        A = A[-1] + A[:-1]
        count +=1
        if A==B:
            return count
        i+=1
    
    return -1