def solution(s):
    if s[0]==')':
        return False

    while s:
        index = 0
        left_count = 0
        item = '('
        while item !=')':
            left_count +=1
            index +=1
            item = s[index]

        left_s = s[:index]
        right_s = s[index:index+left_count]
        for i in range(left_count):
            if ord(left_s[i])+1 != ord(right_s[i]):
                return False

        s = s.replace(left_s+right_s,"",1)
    
    return True
