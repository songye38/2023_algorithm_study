def solution(arr, queries):
    answer = []
    for s,e,k in queries:
        new_array = [i for i in arr[s:e+1] if i>k]
        if new_array:
            answer.append(min(new_array))
        else:
            answer.append(-1)
    return answer