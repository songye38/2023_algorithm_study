import sys
input = sys.stdin.readline

N,M = map(int,input().split())
distance = [[sys.maxsize for j in range(N+1)] for i in range(N+1)]

#0번째 인덱스부터 저장하지 않음. 1번부터 저장함. 
for i in range(1,N+1):
    distance[i][i]  = 0

#친구 관계이므로 양방향 저장을 해주어야 한다. 
for _ in range(M):
    S,E = map(int,input().split())
    distance[S][E] = 1
    distance[E][S] = 1

#항상 K->I->J순서대로 루프를 돌려야 한다. 
# ! 1번 인덱스부터 시작하도록!

for k in range(1,N+1):
    for i in range(1,N+1):
        for j in range(1,N+1):
            if distance[i][j] > distance[i][k] + distance[k][j]:
                distance[i][j]  =  distance[i][k] + distance[k][j]

Min = sys.maxsize
Answer = -1

for i in range(1,N+1):
    temp = 0
    for j in range(1,N+1):
        temp += distance[i][j]

    if Min > temp: #temp값을 최대로 잡았으므로 항상 더 작은 값으로 교체되도록 한다. 
        Min = temp
        Answer = i #! 중요한 건 값 자체를 반환하는게 아니라 그 값의 행 번호를 출력하는 것!



