def solution(s, n):
    answer = ""
    for char in s:
        if char.isupper():
            if ord(char)+n>90:
                answer += chr(ord(char)+n-26)
            else:
                answer += chr(ord(char)+n)
        elif char.islower(): 
            if ord(char)+n>122 :
                answer += chr(ord(char)+n-26)
            else:
                answer += chr(ord(char)+n)
        else:
            answer += ' '
    return answer