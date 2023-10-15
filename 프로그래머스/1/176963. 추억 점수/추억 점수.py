def solution(name, yearning, photo):
    answer = []
    for pho in photo:
        sum = 0
        for person in pho:
            if person in name:
                sum += yearning[name.index(person)]
            else:
                pass
        answer.append(sum)
    return answer