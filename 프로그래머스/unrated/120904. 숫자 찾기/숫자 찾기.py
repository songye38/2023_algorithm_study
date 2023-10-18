def solution(num, k):
    num = [int(i) for i in list(str(num))]
    if k in num:
        return num.index(k)+1
    else:
        return -1
