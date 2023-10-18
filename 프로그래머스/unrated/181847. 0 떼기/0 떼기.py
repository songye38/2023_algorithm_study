def solution(n_str):
    index = 0
    for i in n_str:
        if int(i)==0:
            index +=1
        else:
            break
    
    return n_str[index:]