def solution(cipher, code):
    cipher = '0'+cipher
    answer = ""
    for i in range(len(cipher)):
        if i % code==0:
            answer += cipher[i]
    return answer[1:]