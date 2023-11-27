def getResult(money):
    if len(money)==3:
        return max(money)
    
    if len(money)==4:
        return [money[0]+money[2], money[1]+money[3]]
    
    temp = [i+money[0] for i in getResult(money[2:])]
    temp.append(money[1])
    return temp
                  

def solution(money):
    temp_answer = []
    for i in range(len(money)-2):
        temp_answer.append(max(getResult(money[i:])))

    print(temp_answer)
    return max(temp_answer)




solution([1, 2, 3, 1,3,2])