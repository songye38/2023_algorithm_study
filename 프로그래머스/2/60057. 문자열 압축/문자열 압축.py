def get_split_num(num:int,s:str):
    result = {}
    do_reset = False
    answer = ""
    result[s[:num]] = 1
    for i in range(num,len(s),num): #s[i:i+num]
        if s[i:i+num] not in result:
            key = list(result.keys())[0]
            count = str(result[key])
            if count =='1':
                answer +=key
            else:
                answer += str(result[key]) +key
            result = {}
            result[s[i:i+num]] = 1
        else:
            result[s[i:i+num]] += 1
    if result:
        key = list(result.keys())[0]
        count = str(result[key])
        if count =='1':
            answer +=key
        else:
            answer += str(result[key]) +key
    return len(answer)
            
def solution(s):
    
    max = len(s)
    print(max)
    
    for i in range(1,len(s)+1):
        val = get_split_num(i,s)
        if max > val:
            max = val
    
    return max