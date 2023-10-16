def solution(my_string, s, e):
    if s==e:
        return my_string
    else:
        return my_string[:s] + my_string[s:e+1][::-1]+ my_string[e+1:]