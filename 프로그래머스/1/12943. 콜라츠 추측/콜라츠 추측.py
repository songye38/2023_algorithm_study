def solution(num):
    if num==1:
        return 0
    count = 0
    while num!=1:
        if num %2==0:
            num /=2
            count +=1
        elif num %2!=0:
            num = (num*3)+1
            count +=1
    if count >500:
        return -1
    else:
        return count