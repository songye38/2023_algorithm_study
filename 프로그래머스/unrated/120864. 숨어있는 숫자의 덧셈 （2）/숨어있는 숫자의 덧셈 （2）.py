def solution(my_string):
    answer =0
    my_string = list(my_string)
    for i in range(len(my_string)):
        if not my_string[i].isdigit():
            my_string[i] = '-'
    my_string = "".join(my_string).split('-')
    for i in my_string:
        if i:
            answer += int(i)
    return answer