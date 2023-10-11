def solution(left, right):
    answer = [i for i in range(left,right+1)]
    answer_list = []
    for i in answer:
        count = 0
        for j in range(1,i+1):
            if i % j ==0:
                count +=1
        if count %2==0:
            answer_list.append(+i)
        else:
            answer_list.append(-i)
            
    return sum(answer_list)