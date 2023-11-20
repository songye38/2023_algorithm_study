def solution(record):
    dictionary = {}
    answer = []
    for re in record:
        msg = re.split()
        if msg[0] =='Enter' or msg[0]=='Change':
            dictionary[msg[1]] = msg[2]
            
    for re in record:
        msg = re.split()
        if msg[0] =='Enter':
            a = dictionary[msg[1]]+"님이 들어왔습니다."
            answer.append(a)
        elif msg[0] =='Leave':
            a = dictionary[msg[1]]+"님이 나갔습니다."
            answer.append(a)
    return answer