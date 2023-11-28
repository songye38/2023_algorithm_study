def solution(prices):
    prices.pop()
    answer = []
    for i in range(len(prices)-1):
        count = 1
        num = prices[i]
        for j in range(i+1,len(prices)):
            if num <= prices[j]:
                count+=1
            else:
                break
        answer.append(count)
    answer.append(1)
    answer.append(0)
    return answer