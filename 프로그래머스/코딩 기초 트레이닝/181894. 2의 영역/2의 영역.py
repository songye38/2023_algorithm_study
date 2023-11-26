def solution(arr):
    answer = [i for i in range(len(arr)) if arr[i]==2]
    if not answer:
        return [-1]
    elif len(answer)==1:
        return [2]
    else:
        return arr[min(answer):max(answer)+1]