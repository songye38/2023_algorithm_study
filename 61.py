import sys
input = sys.stdin.readline

N = int(input())
M = int(input())
distance = [[sys.maxsize for j in range(N+1)] for i in range(N+1)]


for i in range(1,N+1):
    distance[i][i] = 0


for _ in range(M):
    start,end,price = map(int,input().split())
    if distance[start][end] > price:
        distance[start][end] = price

for k in range(N+1):
    for i in range(N+1):
        for j in range(N+1):
            if distance[i][j] > distance[i][k] + distance[k][j]:
                distance[i][j] = distance[i][k] + distance[k][j]

for i in range(1,N+1):
    for j in range(1,N+1):
        if distance[i][j]==sys.maxsize:
            print(0,end=' ')
        else:
            print(distance[i][j],end=' ')
    print()


