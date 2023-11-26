def getShortCount(m,n,map,answer): #m,n에서 시작
    if m==0 and n==0:
        return True
    
    if map[n][m-1]==0 and n>=0 and m-1 >=0:
        if getShortCount(m-1,n,map,answer): #왼쪽
            answer.append(1)
    if map[n-1][m] ==0 and n-1>=0 and m >=0:
        if getShortCount(m,n-1,map,answer): #윗쪽
            answer.append(1)


def solution(m, n, puddles):
    answer = []
    map = [[0 for j in range(m)] for i in range(n)] #전체 지도 생성
    for paddle in puddles:
        map[paddle[1]-1][paddle[0]-1] = 1 #물에 잠긴 지역은 1로 표시      
    getShortCount(m-1,n-1,map,answer)
    return len(answer)


print(solution(4,3,[[2, 2]]))