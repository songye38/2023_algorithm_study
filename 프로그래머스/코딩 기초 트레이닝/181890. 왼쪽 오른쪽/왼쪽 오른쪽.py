def solution(str_list):
    
    if 'l' not in str_list and 'r' not in str_list:
        return []
    
    for i in range(len(str_list)):
        print("case here")
        if str_list[i]=='l':
            return str_list[:i]
        elif str_list[i]=='r':
            return str_list[i+1:]