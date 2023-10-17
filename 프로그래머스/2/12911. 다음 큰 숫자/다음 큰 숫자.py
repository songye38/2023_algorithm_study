def get_hex_count(n):
    answer = []
    while n!=0:
        n,remainder = divmod(n,2)
        answer.append(str(remainder))
    return answer.count('1')


def solution(n):
    count_hex_n = get_hex_count(n)
    for i in range(n+1,1000000):
        if count_hex_n == get_hex_count(i):
            return i