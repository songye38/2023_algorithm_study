def solution(arr):
    current = ""
    answer = []
    for i in arr:
        if current != i:
            answer.append(i)
            current = i
    return answer