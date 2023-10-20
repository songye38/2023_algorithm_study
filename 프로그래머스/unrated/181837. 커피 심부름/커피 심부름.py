def solution(order):
    ame = 0
    latte = 0
    for item in order:
        if 'americano' in item:
            ame +=1
        elif 'cafelatte' in item:
            latte +=1
        else:
            ame +=1
        
    return ame * 4500 + latte * 5000