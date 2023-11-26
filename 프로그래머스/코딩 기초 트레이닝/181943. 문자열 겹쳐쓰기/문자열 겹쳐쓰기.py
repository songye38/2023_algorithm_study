#replace 함수를 쓰게 되면 'aaaaaa'와 같이 같은 문자가 있을때 전부 치환된다. 
    #my_string = my_string.replace(replace_string,overwrite_string)

def solution(my_string, overwrite_string, s):
    over_len = len(overwrite_string) #overwrite할 string의 길이
    answer = my_string[:s] + overwrite_string + my_string[s+over_len:]
    return answer