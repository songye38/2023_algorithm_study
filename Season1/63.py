import sys
input = sys.stdin.readline

N,M = map(int,input().split())
distance = [[sys.maxsize for j in range(N+1)] for i in range(N+1)]

for i in range(1,N+1):
    distance[i][i]  = 0

#3 2
for _ in range(M):
    S,E = map(int,input().split())
    distance[S][E] = 1
    distance[E][S] = 1

for k in range(N):
    for i in range(N):
        for j in range(N):
            if distance[i][j] > distance[i][k] + distance[k][j]:
                distance[i][j]  =  distance[i][k] + distance[k][j]

Min = sys.maxsize
Answer = -1

for i in range(N):
    temp = 0
    for j in range(N):
        temp += distance[i][j]
    if Min > temp:
        Min = temp
        Answer = i



