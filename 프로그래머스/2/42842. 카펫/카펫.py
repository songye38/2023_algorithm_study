def solution(brown, yellow):
    answer = []
    total = brown + yellow
    for i in range(3,total//2):
        if total % i==0:
            answer.append([total//i,i])
    for width,height in answer:
        if (width -2) * (height -2) == yellow:
            return [width,height]