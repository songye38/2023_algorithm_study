def solution(binomial):
    temp =''
    if '+' in list(binomial):
        temp = binomial.split('+')
        return int(temp[0]) + int(temp[1])
    elif '-' in list(binomial):
        temp = binomial.split('-')
        return int(temp[0]) - int(temp[1])
    elif '*' in list(binomial):
        temp = binomial.split('*')
        return int(temp[0]) * int(temp[1])
