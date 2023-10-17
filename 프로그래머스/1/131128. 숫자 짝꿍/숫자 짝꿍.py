def solution(X, Y):
    answer = []
    arr_X = [0] * 10
    arr_Y = [0] * 10
    
    for i in list(X):
        arr_X[int(i)] +=1
    
    for i in list(Y):
        arr_Y[int(i)] +=1
    
    for i in range(10):
        if arr_X[i]!=0 and arr_Y[i]!=0:
            times = min(arr_X[i],arr_Y[i])
            for _ in range(times):
                answer.append(str(i))
    answer.sort(reverse=True)    
    
    if not answer:
        return "-1"
    elif sum([int(i) for i in answer])==0:
        return "0"
    else:
        return "".join(answer)