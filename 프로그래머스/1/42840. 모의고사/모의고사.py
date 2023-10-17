def get_max_score(answers,answer_pattern):
    
    user1_answers = answer_pattern
    user1_count = 0
    len_u1 = len(user1_answers)
    
    if len(answers) <= len(user1_answers):
        for i in range(len(answers)):
            if answers[i] == user1_answers[i]:
                user1_count +=1
    else:
        for i in range(len(answers)//len_u1):
            for j in range(len_u1):
                if answers[len_u1 * i + j] == user1_answers[j]:
                    user1_count +=1
        for i in range(len(answers)%len_u1):
            if answers[(len_u1 * (len(answers)//len_u1))+i]== user1_answers[i]:
                user1_count +=1
    return user1_count
    
    
def solution(answers):
    answer = []
    user1 = get_max_score(answers,[1,2,3,4,5])
    user2 = get_max_score(answers,[2, 1, 2, 3, 2, 4, 2, 5])
    user3 = get_max_score(answers,[3, 3, 1, 1, 2, 2, 4, 4, 5, 5])
    score_list = [user1,user2,user3]
    max_val = max(score_list)
    for i in range(3):
        if score_list[i] == max_val:
            answer.append(i+1)
    return answer
    
    
    
    
    
    
    
    