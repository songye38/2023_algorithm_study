answer = 0
def split_s(s):
    if len(s)==1:
        return 
    global answer
    answer +=1
    x = s[0]
    count_x = 0
    count_not_x = 0
    for i in range(0,len(s)):
        if s[i]==x:
            count_x +=1
            if count_x == count_not_x and len(s)>2:
                split_s(s[i+1:])
                break
        else:
            count_not_x +=1
            if count_x == count_not_x and len(s)>2:
                split_s(s[i+1:])
                break
    
def solution(s):
    split_s(s)
    print(answer)

solution("abracadabra")