def solution(arr, k):
    if len(arr)==1:
        return arr
    answer = []
    index = 0
    while index <len(arr):
        if arr[index] not in answer:
            answer.append(arr[index])
            index +=1
        else:
            index +=1
            
        if len(answer)==k:
            break
            
    if len(answer)<k:
        answer += [-1] * int(k-len(answer))
    
    return answer
        