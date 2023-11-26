def solution(array, height):
    answer =  [i for i in array if i>height]
    return len(answer)