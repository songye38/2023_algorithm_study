def solution(n):
    answer = 0
    temp=  [1] * (n+1)
    for i in range(2,int(n**0.5)+1):
        for j in range(i+i , n, i):
            if temp[j]==1:
                temp[j]= 0
                
    temp = [i for i in range(2,n) if temp[i]==True]
    for i in temp:
        if n%i==0:
            print(n,i)
            answer +=1
    if n%2!=0:
        answer +=1
            
    return answer
        