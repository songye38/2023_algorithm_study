def solution(my_string):
    answer = [0] * 52
    for char in my_string:
        if char.isupper():
            answer[ord(char)-65] = my_string.count(char)
        else:
            answer[ord(char)-65-6] = my_string.count(char)
    return answer