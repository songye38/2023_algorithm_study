def make_one(n):
    count = 0
    while n!=1:
        if n%2==0:
            n = n / 2
            count +=1
        else:
            n = (n-1) / 2
            count +=1
    return count

def solution(num_list):
    answer = 0
    for num in num_list:
        answer += make_one(num)
    return answer