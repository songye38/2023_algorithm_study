def solution(numbers, k):
    answer = 0 #k로 트래킹
    curr_index = 0
    while answer != k:
        curr_index += 2
        if curr_index >= len(numbers):
            curr_index = curr_index - len(numbers)
            answer +=1
        else:
            answer += 1
    curr_index -= 2
    return numbers[curr_index]