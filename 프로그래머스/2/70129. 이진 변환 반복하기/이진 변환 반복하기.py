function_call = 0
def to_binary(x):
    global function_call
    function_call += 1
    answer = ""
    c = len(x)
    while c!=0:
        c,remainder = divmod(c,2)
        answer += str(remainder)
        
    answer = answer[::-1]
    return answer
    
def solution(s):
    total_count = 0
    total_count += s.count('0')
    s = s.replace('0',"")
    answer = to_binary(s)
    while len(answer)!=1:
        total_count += answer.count('0')
        answer = answer.replace('0',"")
        answer = to_binary(answer)
    
    return [function_call, total_count]