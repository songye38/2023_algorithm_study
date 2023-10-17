def solution(s):
    result = ''
    capitalize_next = True  # 다음 문자를 대문자로 바꿀지 여부를 나타내는 플래그

    for char in s:
        if char.isspace():
            result += char  
            capitalize_next = True  
        elif capitalize_next:
            result += char.upper()  
            capitalize_next = False 
        elif char.isdigit():
            result += char
        elif not capitalize_next:
            if char.isupper():
                result += char.lower()
            else:
                result += char  

    return result

            
    
    
    
    
    
    
    