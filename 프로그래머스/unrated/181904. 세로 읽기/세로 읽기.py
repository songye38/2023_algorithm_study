def solution(my_string, m, c):
    if m==1: return my_string
    if len(my_string)==1:
        return my_string
    my_string = [my_string[m*i:m*(i+1)] for i in range(len(my_string)//m)]
    answer = ""
    for i in my_string:
        answer += i[c-1]
    
    return answer