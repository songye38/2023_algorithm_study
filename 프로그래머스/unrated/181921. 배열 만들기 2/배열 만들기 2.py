def solution(l, r):
    answer = []
    b = {'5','0'}
    numbers= [i for i in range(l,r+1) if i%5==0]
    for num in numbers:
        if len(set(str(num))-b)==0:
            answer.append(num)
    if answer:
        return answer
    else:
        return [-1]
        