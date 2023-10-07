def solution(array):
    #최빈값이 담긴 배열 만들기 
    answer_array = [0] * (max(array)+1)
    for i in array:
        answer_array[i] = array.count(i)
        
    print(answer_array)
        
    max_value = max(answer_array) #최빈값 수 자체를 구하기 
    answer = answer_array.count(max_value) #최빈값이 겹치는지 확인하기 
    
    
    if answer ==1 :  #최빈값이 한개라면 최빈값의 인덱스를 리턴
        return answer_array.index(max_value)
    else: #최빈값이 겹친다면 -1을 리턴
        return -1
    
    
    
    
    
    
    