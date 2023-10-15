def hex_to_num(num,length):
    result = ""
    remainder = 0
    while num!=0:
        num, remainder = divmod(num,2)
        result += str(remainder)
    result = result[::-1]
    if len(result)!=length:
        result = "0" * (length - len(result)) + result
    return result
    


def solution(n, arr1, arr2):
    map = []
    answer = []
    for i in range(n):
        map.append([hex_to_num(arr1[i],n),hex_to_num(arr2[i],n)])
        
    for row in map:
        temp = ""
        for i in range(n):
            if row[0][i] =='0' and row[1][i]=='0':
                temp += " "
            else:
                temp +='#'
        answer.append(temp)
    return answer
                
    
    
    
    
    
    
    
    
    