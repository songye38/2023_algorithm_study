def solution(my_string, alp):
    answer = ''
    for char in my_string:
        if char==alp:
            my_string = my_string.replace(char,char.upper())
    return my_string