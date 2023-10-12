def solution(n):
    answer = ""
    sum = 0
    #3진법으로 변환하기 
    while n != 0:
        n, remainder = divmod(n,3)
        answer += str(remainder)
    print(answer)
    
    #10진법으로 표현하기 
    j = 0
    for i in range(len(answer)-1,-1, -1):
        sum += int(answer[i]) * (3 ** j)
        j += 1
    return sum
    