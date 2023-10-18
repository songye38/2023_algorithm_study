def to_hex(bin):
    answer = ""
    while bin!=0:
        bin, remainder = divmod(bin,2)
        answer += str(remainder)
    answer = answer[::-1]
    return answer


def solution(bin1, bin2):
    answer = to_hex(int(bin1,2)+int(bin2,2))
    if answer:
        return answer
    else:
        return "0"
