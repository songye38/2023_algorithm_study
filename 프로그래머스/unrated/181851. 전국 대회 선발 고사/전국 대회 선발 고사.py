def solution(rank, attendance):
    answer = []
    for i in range(1,len(rank)+1):
        if attendance[rank.index(i)]==True:
            answer.append(rank.index(i))
        if len(answer)==3:
            break
    return (10000 * answer[0]) + (100 * answer[1]) + answer[2]